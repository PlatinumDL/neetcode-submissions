class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #Max_heap
        max_heap = []
        for stone in stones:
            max_heap.append(-stone)
        
        #Heapify max_heap
        heapq.heapify(max_heap)
        while len(max_heap) > 1:
            #Retrieve two largest stones
            largest = -1 * heapq.heappop(max_heap)
            secondlargest = -1 * heapq.heappop(max_heap)

            if largest == secondlargest: #Destroy
                pass
            else:
                newStone = largest - secondlargest
                #Add to heap
                heapq.heappush(max_heap,-1*newStone)
        
        if len(max_heap) == 1:
            return -1*max_heap[0]
        else:
            return 0