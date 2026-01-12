students_scores = [
    {"name": "鈴木", "score": 92},
    {"name": "田中", "score": 68},
    {"name": "佐藤", "score": 88},
    {"name": "山田", "score": 75},
    {"name": "高橋", "score": 95},
]

# 空のリストを作成
pass_list = []
retake_list = []

# 判定ループ
for student in students_scores:
    if student["score"] >= 80:
        pass_list.append(student["name"])
    else:
        retake_list.append(student["name"])

# 結果表示
print("合格者リスト:", pass_list)
print("追試者リスト:", retake_list)