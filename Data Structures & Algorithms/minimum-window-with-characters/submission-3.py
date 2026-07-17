class Solution:
    def minWindow(self, s: str, t: str) -> str:
        output = ""
        tDict = {}
        windowDict = {}

        if len(t) > len(s):
            return output
        
        for i in t:
            tDict[i] = tDict.get(i,0) + 1

        #Build initial window
        for i in range(len(t)):
            windowDict[s[i]] = windowDict.get(s[i],0) + 1
        
        left = 0
        right = len(t) - 1
        
        while right < len(s):
            #Check subset -> If true, move left until no longer subset
            subset = 0
            for i in windowDict:
                if i in tDict and windowDict.get(i,0) >= tDict.get(i,0):
                    subset += 1

            if subset == len(tDict):
                #Make output
                builder = ""
                for i in range(left,right+1):
                    builder = builder + s[i]
                if output == "" or len(builder) < len(output):
                    output = builder
                
                #Move Left
                if windowDict[s[left]] == 1:
                    windowDict.pop(s[left])
                else:
                    windowDict[s[left]] -= 1
                left += 1
            
            #If false, move right until found subset
            else:
                right += 1
                if right < len(s):
                    windowDict[s[right]] = windowDict.get(s[right],0) + 1
        
        return output


        
        