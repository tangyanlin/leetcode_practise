class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 0: return intervals
        res = []
        intervals.sort(key=lambda x:x[0])  # 按照起始点大小排序
        intervals.append([float('inf'), 0])  # 最后append一个区间  
        
        for i in range(1, len(intervals)):
            if intervals[i][0] <= intervals[i-1][1]:
                # 当前区间和前面区间重合了 合并当前区间和前面一个区间->当前区间
                intervals[i][0] = min(intervals[i-1][0], intervals[i][0])
                intervals[i][1] = max(intervals[i-1][1], intervals[i][1])
            else:
                # 没有重叠 就把前一个区间append  因为当前区间还需要和后面区间对比
                # 最后一个区间和【float('inf'), 0】对比float('inf)可到小于前一个区间的右部分
                # 所以最后一个区间也必会append进来
                res.append(intervals[i-1])
        return res
