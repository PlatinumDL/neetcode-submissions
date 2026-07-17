class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {} # number -> occurence (1 appears 3 times 1:3)
        #Build output array
        dat = [0] * (len(nums) + 1)
        
        #Loop through list of nums and build frequency table
        for i in range(len(nums)):
            if nums[i] not in freq:
                freq[nums[i]] = 1
            else:
                freq[nums[i]] += 1

        #build dat
        for i in freq:
            occurrence = freq[i]
            if dat[occurrence] == 0:
                dat[occurrence] = [i]
            else:
                dat[occurrence].append(i)
        
        foundCounter = 0
        outputArr = []
        
        #Loop through dat and get top k
        for i in reversed(dat):
            if i != 0 and foundCounter < k:
                #Append to output arr
                #Case 1 - Arr smaller or equal than k
                if len(i) <= k:
                    outputArr.extend(i)
                    foundCounter = foundCounter + len(i)
                #Case 2 - Arr larger than k
                else:
                    difference = k - foundCounter
                    outputArr.extend(i[0:difference])
            
        
        return outputArr



        
            
