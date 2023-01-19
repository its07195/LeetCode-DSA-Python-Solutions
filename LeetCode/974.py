class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        d= defaultdict(int)
        d[0]=1
        cur_sum=0
        res=0
        for n in nums:
            cur_sum+=n
            rem=cur_sum %k
            res +=d[rem]
            d[rem]+=1
        return res
