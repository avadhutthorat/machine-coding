import heapq

def topKFrequentNumbers(arr, k):
    dict = {}
    result = []
    
    for _, num in enumerate(arr):
        value = dict[num] + 1 if num in dict else 1
        dict[num] = value

    for _, num in enumerate(dict):
        print(dict[num], num)
        heapq.heappush(result, (dict[num], num) )
        if len(result) > k:
            heapq.heappop(result)
    result = [t[1] for t in result]
    return result        

print(topKFrequentNumbers([1,1,1,3,2,2,2,4,4, 4], 2))