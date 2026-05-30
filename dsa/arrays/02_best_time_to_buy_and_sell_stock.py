Problem: Best Time to Buy and Sell Stock

Interview Question: "Find maximum profit from buying and selling stock once"

LeetCode: #121

Optimal Approach - Single Pass

Time Complexity: O(n)

Space Complexity: O(1)

def maxProfit(prices):
min_price = float('inf')  # Track lowest price seen so far
max_profit = 0            # Track maximum profit seen so far

for price in prices:  
    if price < min_price:  
        min_price = price  
    elif price - min_price > max_profit:  
        max_profit = price - min_price  

return max_profit

Test

prices = [7, 1, 5, 3, 6, 4]
print(f"Prices: {prices}")
print(f"Max Profit: {maxProfit(prices)}")
