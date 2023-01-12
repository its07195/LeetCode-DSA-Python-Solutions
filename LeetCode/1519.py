class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        d= defaultdict(list)
        for a, b in edges:
            d[a].append(b)
            d[b].append(a)
        res= [0] *n
        def dfs(node, prev):
            count= Counter()
            label = labels[node]
            count[label] =1
            for child in d[node]:
                if child == prev:
                    continue
                count+=dfs(child, node)
            res[node]=count[label]
            return count
        dfs(0,None)
        return res
