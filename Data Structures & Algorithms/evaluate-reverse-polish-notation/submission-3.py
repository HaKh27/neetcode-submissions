class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        result=0
        operator= ['+', '-', '*','/']
        for token in tokens: 
            if stack and token in operator: 
                if token =='+':
                    first = stack.pop()
                    second= stack.pop()
                    result= (first+second)
                elif token=='*':
                    first= stack.pop()
                    second=stack.pop()
                    result= (first*second)
                elif token=='-': 
                    first= stack.pop()
                    second=stack.pop()
                    result= (second-first)
                elif token=='/':
                    first= stack.pop()
                    second= stack.pop()
                    result= int(second/first)
                stack.append(result)
            elif token not in operator:
                token= int(token)
                stack.append(token)

        return stack[-1]