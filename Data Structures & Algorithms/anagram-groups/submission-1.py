class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #For each string, loop through each character and sum via ASCII value
        #Take the sum and check dictionary

        outerDict = {}
        #Looping through all the strs
        for i in range(len(strs)):
            innerDict = {}
            #Looping through each char
            for j in range(len(strs[i])):
                #Initialize a dictionary based on the chars
                if strs[i][j] not in innerDict:
                    innerDict[strs[i][j]] = 1
                else:
                    innerDict[strs[i][j]] += 1

            #Convert to frozenset
            frozenSet = frozenset(innerDict.items())

            if frozenSet not in outerDict:
                outerDict[frozenSet] = [strs[i]]
            else:
                outerDict[frozenSet].append(strs[i])

        tempArr = []
        for k in outerDict: 
            tempArr.append(outerDict[k])
        
        return tempArr






                

