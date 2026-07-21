class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        outputArr = []
        #Return K closest points to origin (minHeap?)
        minHeap = []
        #Convert each x and y into euclidean distance
        for x, y in points:
            dist = math.sqrt(x**2 + y**2) #Distance from origin
            minHeap.append((dist,[x,y])) #Distance, points

        #heapify
        heapq.heapify(minHeap)
        for i in range(k):
            minItem = heapq.heappop(minHeap)
            outputArr.append(minItem[1])

        return outputArr


        