from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return []
        hashmap = defaultdict(int)
        max_len = 0
        for num in nums:
            hashmap[num] += 1
            max_len = max(hashmap[num], max_len)
        res = [[] for i in range(max_len+1)]
        result = []
        for key, v in hashmap.items():
            res[v].append(key)
        for i in range(max_len, 0, -1):
            if len(res[i]) > 0 and len(result)<k:
                result += res[i]
        return result