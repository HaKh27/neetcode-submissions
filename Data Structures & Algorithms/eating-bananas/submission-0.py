import math 
class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #Sort the piles to do binary search 
        piles= sorted(piles)
        left= 1
        right= piles[-1]
        best=right

        while left<=right: 
            mid= (left+right)//2
            hours=0 
            for pile in piles: 
                hours+=math.ceil(pile/mid)
            
            if hours<=h: 
                best=min(mid, best)
                right= mid-1
            else:
                left=mid+1
        
        return best





                    