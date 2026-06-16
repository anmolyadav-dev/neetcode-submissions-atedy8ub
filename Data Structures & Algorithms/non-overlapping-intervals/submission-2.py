class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        erased = set()
        intervals.sort()
        print(intervals)
        compared = intervals[0]
        compared_idx = 0
        for i in range(1,len(intervals)):
            if i in erased:
                continue
            curInterval = intervals[i]
            
            if curInterval[0]<compared[1]:
                if curInterval[1]>compared[1]:
                    erased.add(i)
                elif curInterval[1]<=compared[1]:
                    erased.add(compared_idx)
                    compared=curInterval
                    compared_idx = i
            else:
                compared = curInterval
                compared_idx = i
        # if len(intervals)-1 not in erased:

        print(erased)
        return len(erased)