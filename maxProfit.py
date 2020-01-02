def maxProfit(prices):
    if not prices or len(prices) is 1:
        return 0

    buy_price = prices[0]
    profit = 0
    max_profit = 0

    for price in prices:
        if price < buy_price:
            buy_price = price
        else:
            profit = price - buy_price

        if profit > max_profit:
            max_profit = profit

    return max_profit


prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))
