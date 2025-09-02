import heapq


def kSortedArray(arr, k):
    op = []
    heap = []

    for _, num in enumerate(arr):
        heapq.heappush(heap, num)

        if len(heap) > k:
            pop = heapq.heappop(heap)
            op.append(pop)
    final = [*op, *heap]
    return final


print(kSortedArray([6,5,3,2,8,10,9], 3))    