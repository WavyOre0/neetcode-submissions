class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s) # makes a hashmap counting freq of chars
        maxHeap = []
        for char, cnt in count.items():
            heapq.heappush(maxHeap, (-cnt, char))
        
        prev_char = None
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
        if len(res) != len(s):
            return ""
        return res

