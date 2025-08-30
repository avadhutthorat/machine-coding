from collections import deque

def nearestSmallerToRight(arr):
    stack = deque()
    op = []

    for idx in range(len(arr) - 1, -1, -1):
        num = arr[idx]

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

    return op[::-1]


print(nearestSmallerToRight([4,5,2,10,8]))        