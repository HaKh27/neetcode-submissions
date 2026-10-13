from collections import defaultdict 
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        need_count=defaultdict(int)
        #loop through t's string
        for char in t:
            #tally the char frequency
            need_count[char]+=1

        need=len(need_count) #number of distinct characters
        have=0 

        window_count=defaultdict(int)
        left=0
        best_len=float('inf')
        best_window=""
        
        for right in range(len(s)):
            char=s[right]
            window_count[char]+=1

            if window_count[char]==need_count[char]:
                have+=1
            
            while have==need: 
                if right-left+1<best_len:
                    best_len=right-left+1
                    best_window= s[left:right+1]
                    

                window_count[s[left]]-=1

                if window_count[s[left]]<need_count[s[left]]:
                    have-=1
                
                left+=1
        
        return best_window 
            


        