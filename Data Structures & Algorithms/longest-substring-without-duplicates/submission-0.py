class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        window_set=set()
        max_length=0
        for right in range(len(s)):
            if s[right] not in window_set:
                window_set.add(s[right])
            elif s[right] in window_set:
                while s[right] in window_set:
                    window_set.remove(s[left])
                    left+=1
                window_set.add(s[right])
        
            max_length= max(right-left+1, max_length)
    
    
        return max_length 
                