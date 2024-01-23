class Solution:
    def reverse(self, x: int) -> int:
        if x == 0: return 0
        if x > 0:
            flag = 1 
            s = str(x)
        else:
            flag = -1
            s = str(x)[1:]
        s = s[::-1]
        zero_index = 0
        for i in range(len(s)):
            if s[i] == '0': zero_index += 1
            else: break
        res = flag * int(s[zero_index:])
        return res if -2**31 <= res <= 2**31-1 else 0  
