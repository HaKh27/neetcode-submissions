class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        right= len(heights)-1
        max_area=0
        #AREA:  WIDTH X HEIGHT
        # j-i= WIDTH 
        #HEIGHT= MINIMUM value of height[i] and height[j]
        
        
        while left<right:
            height= min(heights[left],heights[right])
            width= right-left
            area= width*height 
            if area>max_area:
                max_area=area
            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1
            
        return max_area


            