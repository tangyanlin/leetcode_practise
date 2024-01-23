def findKthLargest(self, nums: List[int], k: int) -> int:
    hp = nums[:k]
    heapq.heapify(hp)

    for i in range(k, len(nums)):
        if nums[i] > hp[0]:
            heapq.heappop(hp) 
            heapq.heappush(hp, nums[i])
    return hp[0]
