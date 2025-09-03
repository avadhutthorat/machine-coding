import heapq


def kClosestPointToOrigin(arr, k):
    heap = []

    for _, num in enumerate(arr):
        diff = num[0] ** 2 + num[1] ** 2
        heapq.heappush(heap, (-(diff), num))

        if len(heap) > 2:
            heapq.heappop(heap)
    heap = [t[1] for t in heap]
    return heap   


print(kClosestPointToOrigin([[1,3], [-2,2], [5,8], [0,1]], 2))        