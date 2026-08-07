class Solution:
    def reorganizeString(self, s: str) -> str:
        hmap = Counter(s)
        maxHeap = []
        for char, count in hmap.items():
            heapq.heappush(maxHeap, (-count, char))
        
        prev_char = ""
        prev_count = 0
        res = ""
        while maxHeap:
            count, char = heapq.heappop(maxHeap)
            count += 1
            res += char
            if prev_count < 0:
                heapq.heappush(maxHeap, (prev_count, prev_char))
            prev_count = count
            prev_char = char
        if len(s) != len(res):
            return ""
        return res