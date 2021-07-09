"""
[7,1,5,3,6,4]

1. Being able to only buy ONCE and sell ONCE, find the max profit
2. You must buy BEFORE you sell

Max Profit = (6 - 1) = 5

[7,6,4,3,1] (Never want to end up with negative profit)

Max Profit = (0 - 0) = 0
"""

"""

One decision at a time

int min = Integer.MAX_VALUE;
int maxProfit = 0;

[7, 1, 5, 3, 6, 4]

[2, 4, 1]

loop through each index {
    if (if new minimum, buy) {
        // Buy
        if (array[i] < min) -> min = array[i];
    } else {
        // Sell
        // if difference > profit, make it the new max profit
        if (array[i] - min > maxProfit) -> maxProfit = array[i] - min
    }
}

return maxProfit;

Three possible decisions:
1. Buy (Lowest Price)
2. Sell (Highest Price)
3. Wait (Still would lose money if sold) (Decreasing Array)

"""
# print(max_profit([2, 4, 1]))
# print(max_profit([8, 3, 9, 2, 4])

def max_profit(prices):
    # Buying and selling on same day (length of 1) profits 0. 0 length means 0
    if len(prices) <= 1:
        return 0

    min_value = prices[0]
    max_profit = 0

    for i in prices:
        if(i < min_value):
            min_value = i
        else:
            if i - min_value > max_profit:
                max_profit = i - min_value

    return max_profit


def max_profit_2(prices):
    if len(prices) <= 1:
        return 0

    min_price, total_profit = prices[0], 0

    for price in prices:
        if price < min_price:
            min_price = price
        else:
            if price - min_price > total_profit:
                total_profit = price - min_price

    return total_profit


if __name__ == "__main__":
    print(f"Extra: {max_profit_2([2, 4, 1])}")
    print(f"Extra: {max_profit_2([7, 1, 5, 3, 6, 4])}")
    print(max_profit([2, 4, 1]))
    print(max_profit([7, 1, 5, 3, 6, 4]))
