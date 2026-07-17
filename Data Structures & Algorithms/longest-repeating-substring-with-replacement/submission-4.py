class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = k
        maxFreq = 0
        freqMap = {} # a : 1, b : 2, c : 1 -> Number of unique chars CANNOT EXCEED k.
        for i in range(len(s)):
            cur = s[i]
            if freqMap.get(cur) == None:
                freqMap[cur] = 1
            else:
                freqMap[cur] += 1
        
        for key in freqMap:
            left = 0
            right = 0
            nonKey = 0
            while left < len(s) and right < len(s):
                leftChar = s[left]
                rightChar = s[right]

                if rightChar == key:
                    longest = max(longest, (right-left) + 1)
                    right += 1
                elif nonKey < k:
                    longest = max(longest, (right-left) + 1)
                    nonKey += 1
                    right += 1
                else:
                    if leftChar != key:
                        nonKey -= 1
                    left += 1
        return longest



        