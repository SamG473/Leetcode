class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
    
        mstFreq = []
        counts = {}
        
        for num in nums:
            if num in counts:
                counts[num] += 1 
            else:
                counts[num] = 1 

        while k > 0: 
            mstFreq.append(max(counts, key=counts.get))
            del counts[max(counts, key=counts.get)]
            k -= 1 
        
        
        return mstFreq 
        
        
