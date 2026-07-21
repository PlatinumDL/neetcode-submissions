class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #Make a max heap
        maxHeap = []
        for num in nums:
            maxHeap.append(-num) #Add to max heap arr
        
        heapq.heapify(maxHeap) #Heapify max heap

        #Now pop K times and return
        for i in range(k-1):
            heapq.heappop(maxHeap)

        return -maxHeap[0]
