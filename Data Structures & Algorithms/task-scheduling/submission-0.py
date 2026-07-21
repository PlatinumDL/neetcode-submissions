class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        queue = collections.deque()
        maxHeap = []
        countMap = Counter(tasks)
        time = 0

        for key,count in countMap.items():
            maxHeap.append((-count,key))
        heapq.heapify(maxHeap)

        while len(maxHeap) > 0 or len(queue) > 0:
            time += 1
            #If item at top of queue can be processed, add to max heap
            if len(queue) > 0 and queue[0][2] <= time:
                item = queue.popleft()
                count,key,time = item
                heapq.heappush(maxHeap,(count,key))
            print(queue)
            #Process the max heap and add to queue
            if len(maxHeap) > 0:
                maxItem = heapq.heappop(maxHeap)
                oldCount, key = maxItem
                if oldCount + 1 != 0:
                    queue.append((oldCount+1, key, time+n+1)) #new count, key, time to be processed

        return time