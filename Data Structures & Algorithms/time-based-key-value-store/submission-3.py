class TimeMap:
    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        #Get Map Item -> Item is an array
        if self.timeMap.get(key) == None:
            newArr = []
            newArr.append((key,value,timestamp))
            self.timeMap[key] = newArr
        #Add to back
        else:
            self.timeMap[key].append((key,value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        #No values, return ""
        if self.timeMap.get(key) == None:
            return ""
        #If timestamp larger than back, just return back
        elif self.timeMap[key][-1][2] <= timestamp:
            return self.timeMap[key][-1][1]

        #Do binary search until found
        temp = self.timeMap[key]
        start = 0
        end = len(temp) -1
        while start <= end:
            middle = (start + end) // 2 #target is inside [start,end]
            if temp[middle][2] == timestamp: #found
                return temp[middle][1]
            elif temp[middle][2] > timestamp: #target is inside [start, middle-1]
                end = middle - 1
            else: #target is [middle+1, end]
                start = middle + 1
        #Not inside, return closest value
        if temp[end][2] < timestamp:
            return temp[end][1]
        else:
            return ""