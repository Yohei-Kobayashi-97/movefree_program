import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 元となるデータ(3月の売上が欠損している)
data = {
    '月': ['1月', '2月', '3月', '4月', '5月', '6月'],
    '売上': [300000, 280000, np.nan, 350000, 380000, 320000],  # 3月が欠損
    '客数': [320, 300, 310, 360, 390, 330]
}

# データフレームに変換
df = pd.DataFrame(data)
print(df)

# 売上の平均値（NaNを除外して計算）
mean_sales = df['売上'].mean()

# 欠損値を平均値で補完
df['売上'] = df['売上'].fillna(mean_sales)

# 顧客単価 = 売上 / 客数
df['顧客単価'] = df['売上'] / df['客数']

print(df)

# グラフサイズ指定
fig, ax1 = plt.subplots(figsize=(8, 5))

# 売上（棒グラフ）
ax1.bar(df['月'], df['売上'], color='skyblue', label='売上')
ax1.set_xlabel('月')
ax1.set_ylabel('売上（円）')
ax1.set_title('カフェの月別売上と客数')

# 客数（折れ線グラフ：右側の軸）
ax2 = ax1.twinx()
ax2.plot(df['月'], df['客数'], color='orange', marker='o', label='客数')
ax2.set_ylabel('客数（人）')

# 凡例の表示
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

plt.show()
