class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profits = [0]
        for i in range(n):
            for j in range(i,n):
                if i!=j and prices[j] > prices[i]:
                    res = prices[j] - prices[i]
                    # print(f"{prices[j]} - {prices[i]} = {res}")
                    profits.append(res)
        return max(profits)
