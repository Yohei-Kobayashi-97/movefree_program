import os
print(os.getcwd())
import random
from datetime import datetime

# 今日の日付を取得
today = datetime.today()
date_dir = today.strftime("%Y-%m-%d")     # yyyy-mm-dd 形式（ディレクトリ名）
date_jp = today.strftime("%Y年%m月%d日")  # 〇〇年〇月〇日 形式

# 日付ディレクトリを作成
os.makedirs(date_dir, exist_ok=True)

# 1～100のラッキーナンバーを生成
lucky_number = random.randint(1, 100)

# 書き込む文字列を作成（f-strings）
message = f"{date_jp}のラッキーナンバーは{lucky_number}です！"

# ファイルパスを作成
file_path = os.path.join(date_dir, "kadai4-2.txt")

# ファイルに書き込み
with open(file_path, "w", encoding="utf-8") as file:
    file.write(message)

print("kadai4-2.txt にラッキーナンバーを書き込みました。")