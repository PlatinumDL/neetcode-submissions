class Solution:
    def longestPalindrome(self, s: str) -> str:
        #Memoization? I store substrings in the memo table if it is a palindrome.
        memo = {}
        longest = ""
        
        #Initialize memo table with single ditis
        for i in range(len(s)):
            memo[s[i]] = True

        #Outer loop
        for i in range(len(s)-1,-1,-1):
            #Inner loop
            r = i+1
            while r < len(s):  
                if len(longest) == len(s): #Early cut off if longest palindrome already found
                    return longest
                #Check if i to r is palindrome
                if s[r] == s[i]: #To be a palindrome, r and i must be the same, and the inner substring already a palindrome, else cannot be a palindrome
                    if memo.get(s[i+1:r]) is True: #inner substring is palindrome
                        memo[s[i:r+1]] = True #Store in memo table
                        if len(s[i:r+1]) > len(longest):
                            longest = s[i:r+1]
                    elif r - i == 1:#no inner substring
                        memo[s[i:r+1]] = True
                        temp = s[i:r+1]
                        if len(s[i:r+1]) > len(longest):
                            longest = s[i:r+1]
                
                r += 1


        print(memo)
        if longest == "":
            return s[0]
        return longest


        