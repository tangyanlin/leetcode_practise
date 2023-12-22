from collections import defaultdict
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        s = defaultdict(int)
        for num in nums:
            s[num] += 1
        res = []
        for key, num in s.items():
            if num == 2:
                res.append(key)
        return res