from collections import deque

# Use nearest greater to left logic

def stockSpan(arr):
    stack = deque()
    op = []

    for idx, num in enumerate(arr):
        print(idx, num)
        while len(stack) > 0:
            if stack[-1][0] > num:
                op.append(idx - stack[-1][1])
                stack.append([num, idx])
                break
            else:
                stack.pop()    
        else:
            stack.append([num, idx])
            op.append(1)    

    return op

print(stockSpan([100,80,60,70,60,75,85]))    