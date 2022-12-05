# Best Time to Buy and Sell Stock Leetcode 121
"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
"""

def buySellStock(prices):
    # Initial Values for day we buy, sell & max profit gained
    # SC:O(1)
    buy, sell, maxProfit = 0, 1, 0

    # Loop while sell doesn't pass last element of prices
    # TC:O(n)
    while sell < len(prices):
        # Check if price went up & if selling is profitable
        if prices[buy] < prices[sell]:
            # Calculate Profit
            profit = prices[sell] - prices[buy];
            # Compare with maxProfit & store better profit in maxProfit
            maxProfit = max(maxProfit, profit)
        else:
            # We found better price to buy at
            buy = sell
        # Increment Sell for next iteration
        sell += 1
    
    # Returning maximum profit we could find
    return maxProfit
