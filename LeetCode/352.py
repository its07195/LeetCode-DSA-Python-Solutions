class SummaryRanges:

    def __init__(self):
        self.stream=[]
        self.uniqueness_check= set()

    def addNum(self, value: int) -> None:
        if value not in self.uniqueness_check:
            bisect.insort(self.stream, value)
            self.uniqueness_check.add(value)

    def getIntervals(self) -> List[List[int]]:
        result=[]
        for value in self.stream:
            if result and result[-1][1]+1==value:
                result[-1][1]=value
            else:
                result.append([value, value])
        return result
