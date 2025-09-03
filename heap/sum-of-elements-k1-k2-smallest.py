import heapq

def getSmallest(arr, k):
    op = []
    for _, num in enumerate(arr):
        heapq.heappush(op, -num)
        if len(op) > k:
            heapq.heappop(op)
    print(op)        
    return abs(op[0])

def sumKElements(arr, k1, k2):
    result = []

    smallest = getSmallest(arr, k1)
    smallest2 = getSmallest(arr, k2)

    for idx in range(len(arr)):
        num = arr[idx]
        if num > smallest and num < smallest2:
            result.append(num)

    return result

print(sumKElements([1,3,12,5,15,11], 2, 6))