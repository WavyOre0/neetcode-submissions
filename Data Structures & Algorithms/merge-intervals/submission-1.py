class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key = lambda i : i[0]) # sort by the start value
        res = [intervals[0]]
        #start = []
        #intervals overlap if start is in the range of the earlier intervals
      #l = 0
        for start, end  in intervals[1:]:
            prev = res[-1][1]
            if start <= prev: 
                # intervals overlap
                old_start = res[-1][0]
                res.pop()
                res.append([old_start, max(end, prev)])
            else:
                res.append([start, end])
        return res
            
            
