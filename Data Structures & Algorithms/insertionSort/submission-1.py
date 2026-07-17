# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        if len(pairs) == 0:
            state = []
        else:
            state = [list(pairs)]

        #Loop through unsorted section
        for i in range(1, len(pairs)):
            #Loop through sorted section to find place to insert
            for j in range(i):
                #If pair in unsorted section is smaller, insert at index.
                if pairs[i].key < pairs[j].key:
                    temp = pairs.pop(i)
                    pairs.insert(j, temp)
                    break
            state.append(list(pairs))
        
        return state



            

        