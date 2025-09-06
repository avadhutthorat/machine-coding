def maxSumSubarraySizeK(arr, k):
    maxsum = 0
    sum = 0
    left = 0
    right = 0

    while (right < len(arr)):
        sum += arr[right]      
        if right - left + 1 == k:
            maxsum = max(sum, maxsum)
            sum -= arr[left]
            left += 1
        right += 1
    return maxsum        


print(maxSumSubarraySizeK([2,5,1,8,2,9,9], 3))    