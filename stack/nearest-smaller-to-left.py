from collections import deque

def nearestSmallerToLeft(arr):
    stack = deque()
    op = []

    for _, num in enumerate(arr):
        while len(stack) > 0:
            if(stack[-1] < num):
                op.append(stack[-1])
                stack.append(num)
                break
            else:
                stack.pop()
        else:
            stack.append(num)
            op.append(-1)

    return op                    


print(nearestSmallerToLeft([4,5,2,10,8]))        