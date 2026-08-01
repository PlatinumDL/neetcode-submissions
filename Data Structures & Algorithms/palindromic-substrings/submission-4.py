class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        memo = []
        for i in range(len(s)):
            memo.append([])
            for j in range(len(s)):
                memo[i].append(False)
 
        #Initialize initial palindromes
        for i in range(len(s)):
            count += 1
            memo[i][i] = True

        #Outer Loop
        for i in range(len(s)-1,-1,-1):
            r = i+1
            while r < len(s): #Inner Loop
                left = s[i]
                right = s[r]
                if left == right: #If left and right is equal, then check inside if it is a substring
                    if memo[i+1][r-1] is True:
                        count += 1
                        memo[i][r] = True
                    elif r - i == 1: #Case where theres no inner substring
                        count += 1
                        memo[i][r] = True
                r += 1
        
        return count