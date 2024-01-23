class Solution:
    def countBits(self, n: int) -> List[int]:
        def count_one(x):
            count = 0
            while x:
                if x & 1: count += 1
                x >>= 1
            return count
        res = []
        for i in range(n+1):
            res.append(count_one(i))
        return res
