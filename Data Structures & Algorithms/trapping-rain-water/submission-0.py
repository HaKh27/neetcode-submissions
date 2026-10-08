class Solution:
    def trap(self, height: List[int]) -> int:
        left_max=[height[0]]
        right_max=[0]*len(height)
        right_max[-1]=height[-1]
        for i in range(1,len(height)):
            if height[i]>left_max[i-1]:
                left_max.append(height[i])
            else:
                left_max.append(left_max[i-1])
        
        for i in range(len(height)-2,-1,-1):
            right_max[i]= max(right_max[i+1],height[i])
            
        total=0
        for i in range(len(height)):
            check= min(left_max[i],right_max[i])-height[i]
            if check>0: 
                total+= check
            

        return total 
