class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        subDict = {}

        l = 0
        r = 1

        if len(s) == 0 or len(s) == 1:
            return len(s)

        subDict[s[l]] = 1
        while r < len(s) and l < len(s):
            left = s[l]
            right = s[r]
            
            #Found duplicate, move l until no duplicate
            if subDict.get(right) != None and l != r:
                subDict[left] = None
                l += 1
            #Not duplicate, update dict and move r
            else:
                subDict[right] = 1
                #Check longest every iteration
                longest = max(longest,(r-l)+1)
                r += 1

        return longest

        