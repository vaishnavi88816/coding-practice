"""
Problem: Best Time to Buy and Sell Stock

Description:
Given a list of stock prices where each element represents the stock price on a particular day,
find the maximum profit that can be earned by buying once and selling once.
If no profit is possible, return 0.

Example:
Input:
7 1 5 3 6 4

Output:
5

Approach:
- Keep track of the minimum price seen so far.
- For each new price, calculate the profit if the stock is sold today.
- Update the maximum profit whenever a larger profit is found.

Time Complexity: O(n)
Space Complexity: O(1)
"""

prices = list(map(int, input("Enter stock prices: ").split()))

min_price = prices[0]
max_profit = 0

for price in prices[1:]:

    # Update the minimum buying price
    if price < min_price:
        min_price = price

    else:
        # Calculate profit if sold today
        current_profit = price - min_price

        # Update maximum profit
        if current_profit > max_profit:
            max_profit = current_profit

print("Maximum Profit:", max_profit)