class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        def dfs(w,i):
            n=len(w)
            if i==n:
                self.res.append(w)
                return
            for j in range(i, n+1):
                if w[i:j] in words_set and (i>0 or j!=n) and j not in visited:
                    visited.add(j)
                    dfs(w,j)
        words_set= set(words)
        self.res=[]
        for w in words:
            visited={0}
            dfs(w, 0)
        return self.res
