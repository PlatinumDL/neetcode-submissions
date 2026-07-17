class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for i in range(len(operations)):
            if operations[i] == "+":
                newSum = int(record[-1]) + int(record[-2])
                record.append(newSum)
            elif operations[i] == "C":
                record.pop()
            elif operations[i] == "D":   
                newProduct = int(record[-1]) * 2
                record.append(newProduct)
            else:
                record.append(operations[i])
        output = 0
        for i in range(len(record)):
            output = output + int(record[i])
        return output
