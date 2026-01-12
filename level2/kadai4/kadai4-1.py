import random

# サイコロを10回振る
rolls = [random.randint(1, 6) for _ in range(10)]


# 合計と平均を計算
total = sum(rolls)
average = total / len(rolls)


# 結果を表示
print("出た目:", rolls)
print("合計:", total)
print("平均:", average)