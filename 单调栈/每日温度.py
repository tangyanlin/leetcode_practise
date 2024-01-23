def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    # 实质：找到右侧第一个比当前元素大的数
    length = len(temperatures)
    if length == 0: return []
    if length == 1: return [0]
    stack = []   # 单调递减栈
    res = [0] * length
    for i in range(length):
        # 栈不为空 且 开始上升
        while stack and temperatures[i] > temperatures[stack[-1]]:
            # 找到第一个大于栈顶的原素  res赋值  出栈
            res[stack.pop()] = i - stack[-1]
        # stack为空直接入栈  降序直接入栈
        stack.append(i)
    return res
