class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res =set()
        subseq=[]
        def dfs(i, prev):
            if i==len(nums):
                if len(subseq)>=2:
                    res.add(tuple(subseq))
                return
            dfs(i+1, prev)
            if nums[i]>=prev:
                subseq.append(nums[i])
                dfs(i+1, nums[i])
                subseq.pop()
        dfs(0, -inf)
        return list(res)
