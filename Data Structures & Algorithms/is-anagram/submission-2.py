class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count={}
        for ch in s: 
            count[ch]=count.get(ch,0)+1
        
        count2={}
        for ch in t:
            count2[ch]=count2.get(ch,0)+1
    
        return count==count2

