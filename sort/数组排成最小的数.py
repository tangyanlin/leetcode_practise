class Solution:
    def crackPassword(self, password: List[int]) -> str:
        if not password: return ""
        def quick_sort(password, left, right):
            if left >= right: return 
            temp, i, j = left, left, right
            # 从小到大排列
            while i < j:
                # 右边碰到比它大  j-=1
                while i < j and (password[j]+password[temp]) > (password[temp]+password[j]):
                    j -= 1
                # 左边碰到比它小  i+=1
                while i < j and (password[i]+password[temp]) <= (password[temp]+password[i]):
                    i += 1
                password[i], password[j] = password[j], password[i]
            password[temp], password[i] = password[i], password[temp]
            quick_sort(password, left, i-1)
            quick_sort(password, i+1, right)
        password = list(map(str, password))   # [10,2] -> ['10', '2']
        quick_sort(password, 0, len(password)-1)
        return ''.join(password) 
