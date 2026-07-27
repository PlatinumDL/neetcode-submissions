class Solution:
    def climbStairs(self, n: int) -> int:
        #Find number of ways to reach top of the stair case

        #At step 1 -> 1 possible way
        #At step 2 -> 2 possible ways (1,1 and 2)
        #At step 3 -> 1,1,1 or 2,1 or 1,2 (3 ways)
        #n is top of staircase
        ways = [0] * (n+1)
        ways[0] = 1
        ways[1] = 1

        if n < 2:
            return 1

        for i in range(2,n+1):
            ways[i] = ways[i-1] + ways[i-2]

        return ways[n]