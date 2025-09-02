

import heapq
from collections import deque

def kthSmallestElement(arr, k):
    # Solution 1
    # return heapq.nsmallest(k,arr)[-1]

    # Solution 2
    op = []
    for _, num in enumerate(arr):
        heapq.heappush(op, -num)
        if len(op) > k:
            heapq.heappop(op)
    return abs(op[0])

    # Solution 3
    # stack = deque()
    # op = []

    # for idx, num in enumerate(arr):
    #     if len(stack) == 0:
    #         stack.append(num)
    #     elif stack[-1] > num:
    #         stack.append(num)
    #     else:
    #         stack.appendleft(num)

    #     if len(stack) > k:
    #         stack.popleft()
    # return stack[0]



print(kthSmallestElement([7,10,4,3,20,15], 3))

