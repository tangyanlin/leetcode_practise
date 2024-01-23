class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        if x == 1:
            return 1
        left = 0
        right = int(x/2)+1
        while left < right:
            middle = left + (right -left+1)//2
            res = middle*middle
            if res <= x:
                left = middle
            else:
                right = middle - 1
        return left