class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        res = x ^ y
        dist = 0
        while res:
            dist += res & 1
            res = res >> 1
        return dist