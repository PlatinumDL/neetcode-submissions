class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        output = 0

        for i in range(len(operations)):
            if operations[i] == "+":
                newSum = int(record[-1]) + int(record[-2])
                record.append(newSum)
                output = output + newSum
            elif operations[i] == "C":
                reduce = record.pop()
                output = output - int(reduce)
            elif operations[i] == "D":   
                newProduct = int(record[-1]) * 2
                record.append(newProduct)
                output = output + newProduct
            else:
                record.append(operations[i])
                output = output + int(operations[i])
    
        return output
