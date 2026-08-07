class Solution:
    def reorganizeString(self, s: str) -> str:
        hmap = Counter(s)
        
        maxHeap = []
        for char, count in hmap.items():
            heapq.heappush(maxHeap, (-count, char))

        prev_char = ""
        prev_cnt = 0
        res = ""
        while maxHeap:
            cnt, char = heapq.heappop(maxHeap)
            cnt += 1
            res += char
            if prev_cnt != 0:
                heapq.heappush(maxHeap, (prev_cnt, prev_char))
            prev_char = char
            prev_cnt = cnt
        
        if len(s) != len(res):
            return ""
        return res