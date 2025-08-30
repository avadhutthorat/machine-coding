from collections import deque

def nearestGreaterToLeft(arr):
    stack = deque()
    op = []

    for idx, num in enumerate(arr):
        print(idx, num, stack, op, end='\n')

        # if(len(stack) == 0):
        #     stack.append(num)
        #     op.append(-1)
        # else:
        while len(stack) > 0:
            if stack[-1] > num:
                op.append(stack[-1])
                stack.append(num)
                break
            else:
                stack.pop()
        else:
            stack.append(num)
            op.append(-1)      
    return op     
           
print(nearestGreaterToLeft([1,3,2,4]))
