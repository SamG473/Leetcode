class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        most = 0
        lowest = float('inf')
        
        for price in prices:
            if price < lowest:
                lowest = price 
            result = price - lowest
            
            if result > most: 
                most = result
        return most  
        
