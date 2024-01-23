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

        values = [(value, key)for key, value in hashmap.items()]
        hp = values[:k]
        heapq.heapify(hp)
        for i in range(k, len(values)):
            if values[i][0] > hp[0][0]:
                heapq.heappop(hp)
                heapq.heappush(hp, values[i])
        return [h[1]for h in hp] 