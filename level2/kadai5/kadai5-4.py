import numpy as np

scores = np.array([[72, 85],
                   [90, 92],
                   [68, 77],
                   [88, 95],
                   [76, 80]])

# 数学の点数（1列目）だけを抽出する
math_scores = scores[:, 0]
print("数学の点数:", math_scores)

# 3人目の英語の点数（3行2列目）だけを抽出する
third_english = scores[2, 1]
print("3人目の英語の点数:", third_english)

#数学の平均点を計算する
math_average = np.mean(scores[:, 0])
print("数学の平均点:", math_average)

#英語の最高点を計算する
english_max = np.max(scores[:, 1])
print("英語の最高点:", english_max)

#数学の点数が80点以上だった生徒の、数学と英語の両方の点数を抽出する
high_math_scores = scores[scores[:, 0] >= 80]
print("数学が80点以上の生徒の点数:\n", high_math_scores)
