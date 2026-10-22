class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #prefill the array with 0
        result=[0] * len(temperatures)
        stack=[]
        
        for i in range(len(temperatures)):
            #while the stack is NOT EMPTY and the current temp is greater than whatever is appended to the stack on top
            while stack and temperatures[i]> temperatures[stack[-1]]: #36 > 30 = yes 
                #pop the top 
                popped=stack.pop() #0 - #2 
                result[popped]=i-popped #1 -0  --> 3-2 =1 . result[2]=1 

            stack.append(i) #38, 36 , 35, 40

        return result 

 