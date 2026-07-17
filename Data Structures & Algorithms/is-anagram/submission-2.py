class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Initialize dict with String s and t (letters)
        tDict = {}
        sDict = {}
        #Check length first -> must be equal
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if t[i] not in tDict:
                tDict[t[i]] = 1
            if s[i] not in sDict:
                sDict[s[i]] = 1

            tDict[t[i]] += 1
            sDict[s[i]] += 1

        #Check if dict is the same
        if tDict == sDict:
            return True
        else:
            return False



        