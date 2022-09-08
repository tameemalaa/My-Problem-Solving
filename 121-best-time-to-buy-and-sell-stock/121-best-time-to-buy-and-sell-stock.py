class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell , mxp = 0 , 1 ,0 
        while sell < len(prices):
            if prices[buy] >  prices[sell] :
                buy = sell
            else : mxp = max(mxp, prices[sell] - prices[buy])
            sell+=1
        return mxp