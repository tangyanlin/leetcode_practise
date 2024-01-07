class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)-1, -1, -1):
            while len(stack) > 0 and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()
            ans[i] = 0 if len(stack) == 0 else (stack[-1] - i)
            stack.append(i)
        return ans