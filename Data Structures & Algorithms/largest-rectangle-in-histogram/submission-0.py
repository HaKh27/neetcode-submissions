class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        best=0 
        left=0
        for right in range(len(heights)):
            #while stack is not empty and stack[-1]> current val
            while stack and heights[stack[-1]]> heights[right]:
                popped= stack.pop()
                #if stack is empty, set left to -1
                if not stack: 
                    left=-1
                else: 
                    #if its not empty, left is the index at the top of stack 
                    left= stack[-1]
                #height is the val of the index you just popped
                height= heights[popped]
                #calculate width- EXCLUSIVE  (-1) inclusive (+1)
                width= right-left-1 
                #A= Height*width
                area= height*width 
                best= max(best, area)
            #append every element's index to stack regardless. 
            stack.append(right)
    
        #if there's leftover in the stack, clean up
        right= len(heights)
        while stack: 
            popped= stack.pop()
            if not stack: 
                left=-1
            else:
                left= stack[-1]
            height= heights[popped]
            width= right-left-1
            area= height*width 
            best= max(best,area)
    
        return best 
        