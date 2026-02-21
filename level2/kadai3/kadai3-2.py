def calc_payment(total_price: int, rank: str) -> int:

    "商品合計金額（税抜）と会員ランクから最終支払金額（税抜）を計算する"

    discount_rates: dict[str, float] = {
        "gold": 0.20,
        "silver": 0.10,
        "bronze": 0.00
    }

    discount_rate: float = discount_rates.get(rank, 0.0)
    
    discounted_price: float = total_price * (1 - discount_rate)
    tax_included_price: float = discounted_price * 1.10

    return int(round(tax_included_price))


#実行例
print(calc_payment(2000, "gold"))   #1760     
print(calc_payment(1000, "silver")) #990
print(calc_payment(555, "bronze"))  #611
