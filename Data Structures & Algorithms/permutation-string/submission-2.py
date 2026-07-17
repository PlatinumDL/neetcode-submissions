class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Dict = {}
        windowDict = {}
        output = False
        left = 0
        right = len(s1) - 1

        if len(s1) > len(s2):
            return output

        #Build S1 Freq
        for i in s1:
            s1Dict[i] = s1Dict.get(i,0) + 1
        
        #Build first sliding window dict
        for i in range(len(s1)):
            windowDict[s2[i]] = windowDict.get(s2[i],0) + 1
        
        while right < len(s2):
            if windowDict == s1Dict:
                return True
            else:
                #Move right and update windowDict (remove left, add right)
                if windowDict.get(s2[left]) <= 1:
                    windowDict.pop(s2[left])
                else:
                    windowDict[s2[left]] -= 1
                
                right += 1
                left += 1
                if right < len(s2):
                    windowDict[s2[right]] = windowDict.get(s2[right],0) + 1
        
        return output
        