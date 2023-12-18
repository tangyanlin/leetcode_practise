#encoding=utf-8

def array_sub(nums=[1,2,5,2], k =11):
    if k <= 1:
        return 0
    L = 0
    R = 0
    count = 0
    base = 1
    while R < len(nums):
        base *= nums[R]
        while base >= k:
            base /= nums[L]
            L += 1
        count += (R - L + 1)
        R += 1
    return count

print(array_sub())