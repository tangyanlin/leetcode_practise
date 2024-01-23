class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        if k == 0:
            return []
        arr = [-i for i in arr]
        hp = arr[:k]
        heapq.heapify(hp)
        for i in range(k, len(arr)):
            if arr[i] > hp[0]:
                heapq.heappop(hp) 
                heapq.heappush(hp, arr[i])
        
        return [-x for x in hp]