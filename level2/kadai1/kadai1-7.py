# 価格設定
apple_price = 150 #りんご1個150円 
orange_price = 50 #みかん1個50円 

# 個数
the_number_of_apple = 2 #りんご2個
the_number_of_orange = 5 #みかん5個

# 消費税
tax_rate =0.08 #消費税8%

# 小計（税抜）
subtotal = apple_price * the_number_of_apple + orange_price * the_number_of_orange

# 合計（税込）
total = int(subtotal * (1 + tax_rate))  #円なので整数に丸める

# 4人で割る
per_person = total // 4   # 1人あたり
remainder = total % 4     # あまり

# 結果の表示
print("合計金額:", total, "円")
print("1人分の金額:", per_person, "円")
print("あまり:", remainder, "円")