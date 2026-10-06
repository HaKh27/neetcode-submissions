class Solution:

    def encode(self, strs: List[str]) -> str:
        result=""
        for word in strs: 
            length= len(word)
            length= str(length)
            result+= length+"#"+word 
        
        return result

    def decode(self, s: str) -> List[str]:
        result=[]
        i=0

        while i < len(s):
            #find the hash_index using arr.find(what you're looking for, position)
            hash_index= s.find('#',i)
            length= s[i:hash_index] #"5"
            length= int(length) #cast to int 
            content= s[hash_index+1:hash_index+1+length] #find the string 
            result.append(content) #append to result
            i= hash_index+1+length  #move i pointer to next location

        return result