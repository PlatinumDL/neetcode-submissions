class Solution:
    def isPalindrome(self, s: str) -> bool:
        backCounter = len(s) - 1
        frontCounter = 0

        frontStr = ""
        backStr = ""
        #Set to lower case
        s = s.lower()
        
        while backCounter > 0 and frontCounter < len(s):
            #Skip if not alphanumeric 
            if s[backCounter].isalnum() is False: 
                backCounter -= 1
                continue
            if s[frontCounter].isalnum() is False:
                frontCounter += 1
                continue

            frontStr += s[frontCounter]
            backStr += s[backCounter]
            
            #check if it is the same
            if frontStr != backStr:
                return False

            #Traverse
            backCounter -= 1
            frontCounter += 1
        
        return True
        