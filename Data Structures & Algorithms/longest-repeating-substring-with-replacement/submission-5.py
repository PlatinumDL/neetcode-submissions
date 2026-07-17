class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        maxFreq = 0
        freqMap = {} 
        
        left = 0
        right = 0
        while left < len(s) and right < len(s):
            #Count Right
            freqMap[s[right]] = freqMap.get(s[right],0) + 1
            #Update max freq
            maxFreq = max(maxFreq, freqMap[s[right]])
            #Get current window length
            curLength = right - left + 1

            if curLength - maxFreq > k:
                #Reduce Count
                freqMap[s[left]] -= 1
                #Advance Left
                left += 1

            longest = max(longest, (right-left+1))
            right += 1
        return longest



        