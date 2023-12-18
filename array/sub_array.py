#encoding=utf-8

def array_sub(nums=[1,2,5,2], k =11):
    i = 0
    j = 0
    n = len(nums)
    products = 1
    res = 0
    while i < n and j <= n:
        if products < k and j < n:
            products = products * nums[j]
            res += 1
            j += 1
        else:
            products = products / nums[i]
            res += 1
            i += 1
    return res

print(array_sub())