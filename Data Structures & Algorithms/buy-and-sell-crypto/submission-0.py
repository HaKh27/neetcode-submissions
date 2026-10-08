class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price=prices[0]
        max_price=0
        for i in range(1,len(prices)):
            if prices[i]<min_price: 
                min_price=prices[i]
            elif prices[i]>=min_price: 
                total=prices[i]-min_price
                if total>max_price:
                    max_price=total 
        
        return max_price
        