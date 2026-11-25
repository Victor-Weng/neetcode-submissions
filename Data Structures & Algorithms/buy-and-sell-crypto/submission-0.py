class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        leftpass = [0]*len(prices)
        leftpass[0] = prices[0]

        maxprofit = 0

        for i in range(1,len(prices)):
            if prices[i] < leftpass[i-1]:
                leftpass[i] = prices[i]
            else:
                leftpass[i] = leftpass[i-1]
        
        for i in range(len(prices)-1,-1,-1):
            if maxprofit < prices[i] - leftpass[i]:
                maxprofit = prices[i] - leftpass[i]

        return maxprofit
