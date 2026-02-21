correct_number = 30  # 正解

print("1から50までの数字を当ててください！")

while True:
    user_input = int(input("数字を入力してください: "))

    if user_input < correct_number:
        print("もっと大きいです")
    elif user_input > correct_number:
        print("もっと小さいです")
    else:
        print("正解です！")
        break
