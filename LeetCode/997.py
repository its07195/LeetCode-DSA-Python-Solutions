class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        degree={i:0 for i in range(1, n+1)}
        for a, b in trust:
            degree[a]-=1
            degree[b]+=1
        for person, deg in degree.items():
            if deg==n-1:
                return person
        return -1
