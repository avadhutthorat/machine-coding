import heapq

def connectRopesToMinimiseCost(arr):
    heapq.heapify(arr)
    result = 0
    
    while len(arr) > 1:
        top1 = heapq.heappop(arr)
        top2 = heapq.heappop(arr)
        sum = top2 + top1
        result += sum
        heapq.heappush(arr, sum)

    return result



print(connectRopesToMinimiseCost([1,2,3,4,5]))