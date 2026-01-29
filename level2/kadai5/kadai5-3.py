import numpy as np

# ① 0から9までの連続した整数を持つ1次元配列（配列1）
array1 = np.arange(10)

# ② 配列1の全要素を5倍した配列（配列2）
array2 = array1 * 5

# ③ 配列2の中から30以上の要素を抽出した配列（配列3）
array3 = array2[array2 >= 30]

# ④ 配列3の合計値、平均値、要素数を計算
total = array3.sum()
average = array3.mean()
count = array3.size

# 結果の表示
print("配列1:", array1)
print("配列2:", array2)
print("配列3:", array3)
print("合計値:", total)
print("平均値:", average)
print("要素数:", count)