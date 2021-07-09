"""
[7,1,5,3,6,4] = 7
[7,1,5,9,3,6] = 11

[1,5]
[5,1]

[] = 0
[1] = 0
[X,Y] = IF (X < Y) => Y - X
If X < Y -> SOLD (Return some profit)
If X > Y -> DID NOT SELL
[X,Y,Z] =
[1,2,3] = 1 + 1 = 2, (3 - 1) = 2
B,S +1
  B,S +1
        2

[1,5,5]
B,S +4
   B,S +0
          4

Find max profit. Allowed to buy and sell as many times as you want
MUST SELL BEFORE YOU BUY AGAIN
YOU MUST BUY BEFORE YOU SELL

Difference between 1 and 2, is that
1 makes you choose the most
2 allows you to sum up to the most
"""

"""
public int maxProfit(int[] prices) {
    if (prices.length < 2) {
        return 0;
    }
        
    int buyAt = 0;
    int sellAt = 1;
    int maxProfit = 0;
        
    while (sellAt < prices.length) {
        if (prices[sellAt] > prices[buyAt]) {
            maxProfit += prices[sellAt] - prices[buyAt];
        }
        buyAt++;
        sellAt++;
    }
    return maxProfit;
}
"""

def maxProfit(values):
    if len(values) <= 1:
        return 0

    buy_at = values[0]
    max_profit = 0

    # for i in values:
    #     if i < buy_at:
    #         buy_at = i
    #     else:
    #         diff = i - buy_at
    #         max_profit += diff
    #         buy_at = i

    for i in values:
        if i >= buy_at:
            diff = i - buy_at
            max_profit += diff
        buy_at = i

    return max_profit


if __name__ == "__main__":
    print(maxProfit([7, 1, 5, 3, 6, 4]))
    print(maxProfit([7, 1, 5, 9, 3, 6]))
