import requests
from bs4 import BeautifulSoup
import time
import csv
import re
from urllib.parse import urljoin
from typing import List, Tuple

# ユーザーエージェントの設定
HEADERS: dict[str, str] = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

# ぐるなびの全域検索URL
BASE_URL: str = "https://r.gnavi.co.jp/area/jp/rs/?p={}"

def split_address(address: str) -> Tuple[str, str, str, str]:
    """
    住所から郵便番号を除去し、「都道府県」「市区町村」「番地」「建物名」に分割する
    """
    if not address:
        return "", "", "", ""

    # 先頭にある郵便番号（〒100-0006 など）を削除
    address = re.sub(r'^〒?\s*\d{3}-\d{4}\s*', '', address)

    pref_pattern = r'(東京都|北海道|(?:京都|大阪)府|.{2,3}県)'
    city_pattern = r'(.+?市.+?区|.+?区|.+?市|.+?郡.+?[町|村]|.+?郡|.+?町|.+?村)'
    
    pref = ""
    city = ""
    rest = address

    pref_match = re.match(pref_pattern, rest)
    if pref_match:
        pref = pref_match.group(1)
        rest = rest[len(pref):]
        
    city_match = re.match(city_pattern, rest)
    if city_match:
        city = city_match.group(1)
        rest = rest[len(city):]

    # 番地と建物名の分離
    addr_match = re.match(r'([0-9\-−ー一二三四五六七八九十百千\s]+(?:丁目|番地|番|号|[-−ー\d])*|.*?番地.*?号|.*?番地)(.*)', rest)
    
    if addr_match and addr_match.group(1).strip():
        street = addr_match.group(1).strip()
        building = addr_match.group(2).strip()
    else:
        street = rest.strip()
        building = ""
        
    return pref, city, street, building

def check_ssl(url: str) -> bool:
    return url.startswith("https://")

def get_shop_detail(url: str) -> List[str]:
    time.sleep(3)
    try:
        res: requests.Response = requests.get(url, headers=HEADERS, timeout=10)
        # 💡【対策1】文字化け対策：レスポンスの文字コードを「utf-8」に強制固定する
        res.encoding = 'utf-8' 
        res.raise_for_status()
    except Exception as e:
        print(f"店舗ページの取得に失敗しました: {url}")
        return ["", "", "", "", "", "", "", ""]
        
    soup: BeautifulSoup = BeautifulSoup(res.text, "html.parser")

    name_tag = soup.select_one("h1#id_companyName") or soup.select_one(".fn.org") or soup.select_one("p.shop-info__name") or soup.select_one("h1")
    name: str = name_tag.text.strip() if name_tag else ""

    phone_tag = soup.select_one(".tel") or soup.select_one("span.num") or soup.select_one("[itemprop='telephone']")
    phone: str = phone_tag.text.strip() if phone_tag else ""

    address_tag = soup.select_one(".adr") or soup.select_one("span.region") or soup.select_one("[itemprop='address']")
    address: str = address_tag.text.strip() if address_tag else ""
    address = " ".join(address.split())

    pref, city, street, building = split_address(address)

    official_url: str = ""
    links = soup.find_all("a")
    for link in links:
        text: str = link.text.strip()
        href: str | None = link.get("href")
        
        if href and ("ホームページ" in text or "オフィシャル" in text or "公式" in text):
            time.sleep(3)
            try:
                r: requests.Response = requests.get(href, headers=HEADERS, timeout=5, allow_redirects=True)
                official_url = r.url
            except Exception:
                official_url = href
            break

    if official_url:
        ssl: bool = check_ssl(official_url)
        ssl_str: str = "True" if ssl else "False"
    else:
        ssl_str = ""

    return [name, phone, pref, city, street, building, official_url, ssl_str]

def main() -> None:
    shop_data: List[List[str]] = []
    page: int = 1
    seen: set[str] = set()
    
    print("スクレイピングを開始します。目標: 50件")

    while len(shop_data) < 50:
        time.sleep(3)
        url: str = BASE_URL.format(page)
        print(f"一覧ページ {page} へのアクセス中...")
        
        try:
            res: requests.Response = requests.get(url, headers=HEADERS, timeout=10)
            # 💡【対策1】ここも文字コードをutf-8に固定
            res.encoding = 'utf-8'
            res.raise_for_status()
        except Exception as e:
            print(f"一覧ページの取得に失敗しました: {url}")
            break
            
        soup: BeautifulSoup = BeautifulSoup(res.text, "html.parser")
        shop_links = soup.select("a[class*='titleLink']") or soup.select(".style_titleLink__Zg9V_") or soup.select("a.list-rst__rst-name-target")

        if not shop_links:
            shop_links = [a for a in soup.find_all("a", href=True) if "/shop/" in a["href"]]

        if not shop_links:
            print("店舗リンクが見つかりませんでした。")
            break

        for link in shop_links:
            href: str | None = link.get("href")
            if not href:
                continue

            shop_url: str = urljoin("https://r.gnavi.co.jp", href).split("?")[0]

            if "gnavi.co.jp" not in shop_url or "/premium/" in shop_url:
                continue

            if shop_url in seen:
                continue
            seen.add(shop_url)

            if len(shop_data) >= 50:
                break

            print(f"[{len(shop_data) + 1}/50] 店舗詳細を取得中: {shop_url}")
            data: List[str] = get_shop_detail(shop_url)
            
            if data[0]:
                shop_data.append(data)
            
        page += 1

    # 💡【対策2】確実にExcelで開けるようにBOM付きUTF-8（utf-8-sig）で新規書き出し
    output_filename = "shop_data.csv"
    with open(output_filename, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerow(["店舗名", "電話番号", "都道府県", "市区町村", "番地", "建物名", "URL", "SSL"])
        writer.writerows(shop_data[:50])

    print(f"スクレイピングが完了しました。{output_filename} に {len(shop_data[:50])} 件保存しました。")

if __name__ == "__main__":
    main()