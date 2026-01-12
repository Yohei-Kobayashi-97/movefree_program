scores = [88, 92, 75, 88, 95, 68, 88, 70, 65, 96, 72, 85]

# ① scoresの要素数（長さ）を表示
print(len(scores))

# ② 左から2番目から右から2番目までを取り出したリスト
print(scores[1:-1])   # 左から2番目 → index 1、右から2番目 → index -2

# ③ 一番左から一つ飛ばし（2つおき）で取り出したリスト
print(scores[0::2])

# ④ 逆順に並び替えたリスト
print(scores[::-1])

# ⑤ scoresの中に 88 がいくつ含まれているか
print(scores.count(88))

# ⑥ 点数が低い順（昇順）に並び替えたリスト
print(sorted(scores))