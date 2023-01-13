class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        d= defaultdict(list)
        for i, parent in enumerate(parent):
            d[parent].append(i)
        ans =1
        def dfs(node):
            nonlocal ans
            longest= second_longest=0
            for child in d[node]:
                path_length = dfs(child)
                if s[child]!=s[node]:
                    if path_length>longest:
                        second_longest =longest
                        longest=path_length
                    elif path_length > second_longest:
                        second_longest =path_length
            ans = max(ans, longest +second_longest+1)
            return longest +1
        dfs(0)
        return ans
