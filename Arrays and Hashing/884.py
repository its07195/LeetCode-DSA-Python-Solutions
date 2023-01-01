class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s = s1 + ' '+s2
        s = s.split()
        rare = []
        for word in set(s):
            if s.count(word)==1:
                rare.append(word)
        return rare
