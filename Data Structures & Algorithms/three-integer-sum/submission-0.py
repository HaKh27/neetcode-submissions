class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)
        result=[]

        for i in range(len(nums)):
            left= i+1
            right=len(nums)-1

            if i>0 and nums[i]==nums[i-1]:
                continue
                
            while left<right:
                new_r=[]
                current_sum= nums[i]+nums[left]+nums[right]
                if current_sum==0: 
                    new_r.append(nums[i])
                    new_r.append(nums[left])
                    new_r.append(nums[right])
                    result.append(new_r)
                    left+=1
                    right-=1
                    while left<right and nums[left]==nums[left-1]:
                        left+=1

                    while left<right and nums[right]==nums[right+1]:
                        right-=1
                elif current_sum<0:#negative 
                    left+=1
                elif current_sum>0: #positive
                    right-=1
                
            

        return result


            