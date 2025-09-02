import heapq

def frequencySort(arr, k):
    dict = {}
    heap = []
    res = []
    
    for _, num in enumerate(arr):
        value = dict[num] + 1 if num in dict else 1
        dict[num] = value

    for _, num in enumerate(dict):
        heapq.heappush(heap, (dict[num], num) )

    for _, pair in enumerate(heap):
        freq = pair[0]
        num = pair[1]
        res = [*res, *([num] * freq)]
    return res[::-1]      

print(frequencySort([1,1,1,3,2,2,4,], 2))