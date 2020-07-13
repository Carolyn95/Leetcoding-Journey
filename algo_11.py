# best time to buy and sell stock
import pdb
class Solution:
    def maxProfit(self, prices):
        stack = []
        profit = 0
        if len(prices) <= 1:
            return profit
        for p in prices:
            if not stack or p <= stack[-1]:
                stack.append(p)
            else:
                cur_profit = p - stack[-1]
                profit = cur_profit if cur_profit > profit else profit
        print(profit)
        return profit



if __name__ == "__main__":
    s = Solution()
    prices = [7,1,5,3,6,4]
    #prices = [7,6,5,3,2,1]
    s.maxProfit(prices)
    """
    def maxProfit(self, prices):
        length = len(prices)
        max_profit = 0
        if length <= 1:
            print(max_profit)
            return max_profit
        for i in range(length):
            for j in range(i+1, length):
                profit = prices[j] - prices[i]
                max_profit = profit if profit > max_profit else max_profit

        print(max_profit)
        return max_profit

    def maxProfit(self, prices):
        days = len(prices)
        profit = 0
        if days <= 1:
            return profit
        profits = [0] * days
        for day in range(1, days):
            profits[day] = max(profit, prices[day] - min(prices[:day]))
        print(max(profits))
        return max(profits)
    """
