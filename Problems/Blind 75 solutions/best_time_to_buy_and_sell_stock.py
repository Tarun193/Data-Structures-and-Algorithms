"""
Problem Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Problem Statement: 
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Approach:
We will keep track of the profit. If we find a day where the stock price is lower than the previously observed lowest price, we consider buying on that day. We then check if selling in the future would yield a higher profit than the current maximum profit.

Let's debug the example:

Consider buying on 0th day.
current_buy = 7
profit = 0

On 1st day we got stock at  = 1, (current_buy > prices[1]) -> True
current_buy = 1
profit = 0

On 2nd day stock price is 5, our profit is 5 - 1 = 4, (profit < current_profit) -> True
current_buy = 1
profit = 4

On 3rd day stock price is 3, our profit is 3 - 1 = 2, (profit < current_profit) -> False
current_buy = 1
profit = 4

On 4rd day stock price is 6, our profit is 6 - 1 = 5, (profit < current_profit) -> True
current_buy = 1
profit = 5

On 4rd day stock price is 4, our profit is 4 - 1 = 3, (profit < current_profit) -> False
current_buy = 1
profit = 5

So, the maximum profit we can get is 5. 
"""


def maxProfit(prices) -> int:
    # Initially asuming profit is 0.
    profit = 0
    current_buy = prices[0]

    for i in range(len(prices)):
        if current_buy > prices[i]:
            current_buy = prices[i]
            continue
        if profit < prices[i] - current_buy:
            profit = prices[i] - current_buy
    
    return profit