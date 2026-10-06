class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group={}

        for word in strs: 
            sorted_word= sorted(word)
            words="".join(sorted_word)
            group[words]=group.get(words,[])+[word]

        result=[]
        for g in group: 
            result.append(group[g])
        
        return result
        
        
        