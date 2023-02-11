class Solution:
    def shortestAlternatingPaths(self, n: int, r: List[List[int]], b: List[List[int]]) -> List[int]:
        self.res = [float("inf")] * n
        re = [[] for i in range(n) ]
        be = [[] for i in range(n) ]
        for i in r:
            re[i[0]].append(i[1])
        for i in b:
            be[i[0]].append(i[1])
        self.bfs(re,be,False,n)
        self.bfs(re,be,True,n)
        for i in range(len(self.res)):
            if self.res[i] == float('inf'):
                self.res[i]=-1
        return self.res
    def bfs(self,re,be,f,n):
        visited = set()
        queue = [[0,f,0]]
        while queue:
            current,color,step = queue[0]
            queue.pop(0)
            color = not color
            self.res[current] = min(self.res[current],step)
            if color:
                for i in re[current]:
                    if (i,color) not in visited:
                        visited.add((i,color))
                        queue.append([i,color,step+1])
            elif not color:
                for i in be[current]:
                    if (i,color) not in visited:
                        visited.add((i,color))
                        queue.append([i,color,step+1])
