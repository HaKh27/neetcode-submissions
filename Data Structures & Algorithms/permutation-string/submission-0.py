from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #initialize variables
        left=0 
        tally1=defaultdict(int)
        tally2=defaultdict(int)
        
        k= len(s1)
        n= len(s2)

        if k>n: 
            return False

        for i in range(k):
            #increment both freq counts 
            tally1[s1[i]]+=1
            tally2[s2[i]]+=1
        
        if tally1==tally2: 
            return True 

        for right in range(k,n): 
            tally2[s2[right]]+=1
            tally2[s2[left]]-=1

            if tally2[s2[left]]==0: 
                del tally2[s2[left]]
            
            if tally1==tally2:
                return True 
            left+=1

        return False 
          