# Given an array of integers (positive and negative), 
# find the contiguous subarray with the largest sum. Return the sum. 
# The subarray can be of any length, even it could be the whole array. 
# It could be also a single element 
# The function will find that the contiguous subarray with the largest sum is [4, -3, 7, 2, 4], 
# which sums 14. The function should return 14.

A = [4, -3, 7, 2, 4, -5, 1, 2]

def maxSubArray(nums: list) -> int:
    oneSum, maxSum = 0, nums[0]
    for i in range(len(nums)):
        oneSum += nums[i]
        maxSum = max(maxSum, oneSum)
    return maxSum

print(maxSubArray(A))