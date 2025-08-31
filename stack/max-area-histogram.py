from collections import deque

def nearestSmallerToLeft(arr):
    stack = deque()
    op= []

    for idx, num in enumerate(arr):
        while len(stack) > 0:
            if stack[-1][0] < num:
                op.append(stack[-1][1])
                stack.append([num, idx])
                break
            else:
                stack.pop()
        else:
            stack.append([num, idx]) # [num, idx]
            op.append(-1)    

    return op

def nearestSmallerToRight(arr):
    stack = deque()
    op = []

    for idx in range(len(arr) - 1, -1, -1):
        num = arr[idx]
        while len(stack) > 0:
            if stack[-1][0] < num:
                op.append(stack[-1][1])
                stack.append([num, idx]) # [num, idx]
                break
            else:
                stack.pop()
        else:
            stack.append([num, idx]) # [num, idx]
            op.append(len(arr))

    return op[::-1]        


def maxAreaHologram(arr):
    op = []

    NSL = nearestSmallerToLeft(arr)
    NSR = nearestSmallerToRight(arr)

    for idx, num in enumerate(arr):
        NSLid = NSL[idx]
        NSRid = NSR[idx]
        result = (abs(NSLid - NSRid) - 1) * num
        op.append(result)
    return max(op)    


# print(nearestSmallerToLeft([6,2,5,4,5,1,6]))    
# print(nearestSmallerToRight([6,2,5,4,5,1,6]))    
print(maxAreaHologram([6,2,5,4,5,1,6]))    
