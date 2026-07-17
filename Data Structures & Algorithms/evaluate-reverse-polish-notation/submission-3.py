class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        outputVal = 0
        stack = []
        counter = 0
        
        #While stack not empty
        while counter < len(tokens):
            #Check if cur value is an operator
            if tokens[counter] == "+" or tokens[counter] == "-" or tokens[counter] == "*" or tokens[counter] == "/":
                #Evaluate operator (pop top 2)
                top2 = int(stack.pop())
                top1 = int(stack.pop())
                if tokens[counter] == "+":
                    outputVal = top1 + top2
                    stack.append(outputVal)
                elif tokens[counter] == "-":
                    outputVal = top1 - top2
                    stack.append(outputVal)
                elif tokens[counter] == "*":
                    outputVal = top1 * top2
                    stack.append(outputVal)
                else:
                    outputVal = top1 / top2
                    stack.append(outputVal)
                print(top1)
                counter +=1
            #If not operator, add to stack
            else:
                stack.append(tokens[counter])
                counter += 1
            
        if len(stack) > 0:
            return int(stack[0])
        else:
            return outputVal
            

        