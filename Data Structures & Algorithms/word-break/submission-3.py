from functools import cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        start = 0 #Start point for DFS
        @cache
        def dfs(start):
            for word in wordDict:
                #Check if this word is valid
                endPoint = start + len(word)
                if word == s[start:endPoint] and endPoint != len(s): #Valid, continue DFS
                    if dfs(endPoint):
                        return True
                
                elif word == s[start:endPoint] and endPoint == len(s):
                    print("Trigger")
                    return True
            
            return False

        return dfs(start)