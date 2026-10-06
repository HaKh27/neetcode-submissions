class Solution:
    def isPalindrome(self, s: str) -> bool:
        #initialize a new string
        new_str=""
        #loop through string
        for ch in s: 
            #check if the character is an alphabet or number 
            if ch.isalnum():
            #append to new string in lowercase
                new_str+=ch.lower()

        return new_str==new_str[::-1]