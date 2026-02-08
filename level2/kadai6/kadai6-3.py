import requests

# ユーザーから郵便番号を入力してもらう
zipcode = input("7桁の郵便番号を入力（ハイフンなし）: ")


# APIのURL
url = "https://zipcloud.ibsnet.co.jp/api/search"


# パラメータ
params = {
    "zipcode": zipcode
}


# APIへリクエスト送信
response = requests.get(url, params=params)


# JSONデータに変換
data = response.json()


# まずは取得できたデータを確認（デバッグ用）
print("取得したデータ:")
print(data)


# 結果が存在するか確認
if data["results"] is not None:
    result = data["results"][0]

    # 都道府県・市区町村・町域名を取得
    prefecture = result["address1"]
    city = result["address2"]
    town = result["address3"]

    # 住所を整形して表示
    address = f"住所: {prefecture}{city}{town}"
    print(address)
else:
    # 郵便番号が存在しない場合
    print("該当する住所が見つかりませんでした。")