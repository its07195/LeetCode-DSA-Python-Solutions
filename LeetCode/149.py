from decimal import *
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def getAngles(p1, p2):
                # [[0,0],[94911150,94911151],[94911151,94911152]]
                yDiff = p2[1] - p1[1]
                xDiff = p2[0] - p1[0]

                if xDiff == 0:
                    return sys.maxsize

                return Decimal(yDiff) / Decimal(xDiff)


        ans = 0
        n = len(points)

        for i in range(n):
            p1 = points[i]
            same = 0
            angles = []
            for j in range(n):
                if i != j:
                    p2 = points[j]
                    if p1 == p2:
                        same += 1
                    else:
                        angles.append(getAngles(p1, p2))

            counter = Counter(angles)

            max1 = 0
            if counter.values():
                max1 = max(counter.values())

            ans = max(ans, max1 + same + 1)

        return ans
