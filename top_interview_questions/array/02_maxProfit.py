# problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        len_prices = len(prices)
        profit = 0
        if len_prices <= 1:
            return profit

        low = prices[0]
        high = prices[0]
        for price in prices:
            if price > high:
                high = price
            else:
                profit += high - low
                high = low = price

        return profit + high - low


# input
A = [7,1,5,3,6,4]

solution = Solution()
output = solution.maxProfit(A)

# output
print(output)

