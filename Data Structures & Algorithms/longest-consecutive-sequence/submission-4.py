class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        found=set()
        for num in nums:
            found.add(num)

        if len(nums)==0:
            return 0

        result=[]
        count=0
        for num in found: 
            if num-1 not in found: 
                count=1 
                while num+1 in found: 
                    count+=1
                    num=num+1
                result.append(count)
                
        return max(result)
        
        

        