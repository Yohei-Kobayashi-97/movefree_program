# アトラクションに乗れる条件 : 身長120以上　かつ　体重100未満

# 人物データ
A = {"height": 160, "weight": 60}
B = {"height": 120, "weight": 40}
C = {"height": 180, "weight": 100}

# 乗車判定
def can_ride(person):
    return person["height"] >= 120 and person["weight"] < 100

# 結果
print("Aさん：", can_ride(A))
print("Bさん：", can_ride(B))
print("Cさん：", can_ride(C))