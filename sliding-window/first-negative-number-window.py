from collections import deque

def firstNegativeNumberInWindow(arr, k):
    neg = deque()
    op = []
    start = 0

    for _, num in enumerate(arr):
        if num < 0:
            neg.append(num)

    while start < len(arr) - k + 1:
        if len(neg) > 0:
            op.append(neg[0])  
            if(neg[0] == arr[start]):
                neg.popleft()
        else:
            op.append(0)        
        start += 1
    return op     




print(firstNegativeNumberInWindow([12, -1, -7, 8, -16, 30, 16, 28], 3))   
