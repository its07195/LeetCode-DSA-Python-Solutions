class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curMax, maxSum, curMin, minSum, tot = -inf, -inf, inf, inf, 0
        for n in nums:
            curMax= max(n, curMax +n)
            maxSum= max(maxSum, curMax)
            curMin=min(n, curMin+n)
            minSum=min(minSum, curMin)
            tot+=n
        return max(maxSum, tot-minSum) if maxSum>0 else maxSum
