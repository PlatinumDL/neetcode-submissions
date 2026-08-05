#from functools import cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        start = 0 #Start point for DFS
        memo = {}

        def dfs(start):
            if start in memo:
                return memo.get(start)

            for word in wordDict:
                #Check if this word is valid
                endPoint = start + len(word)
                if word == s[start:endPoint] and endPoint != len(s): #Valid, continue DFS
                    if dfs(endPoint):
                        memo[start] = True
                        return True
                
                elif word == s[start:endPoint] and endPoint == len(s):
                    print("Trigger")
                    memo[start] = True
                    return True
            
            memo[start] = False
            return False

        return dfs(start)