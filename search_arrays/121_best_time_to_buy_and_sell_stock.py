class Solution(object):
    def maxProfit(self, prices):
        max_profit = 0
        min_buy = float('inf')
        for price in prices:
            min_buy = min(min_buy, price)
            max_profit = max(max_profit, price - min_buy)
        return max_profit


if __name__ == '__main__':

    prices = [7,1,5,3,6,4]

    ss = Solution()
    res = ss.maxProfit(prices)

    print(res)
