class Solution:
    def reorganizeString(self, s: str) -> str:
        hmap = Counter(s) # this is a hashmap that counts each char and returns the hashmap for it
        maxHeap = []
        for val, count in hmap.items():
            heapq.heappush(maxHeap, (-count, val))

        prev_char = ""
        prev_count = 0
        res = ""
        while maxHeap:
            count, char = heapq.heappop(maxHeap)
            res += char
            count += 1
            if prev_count != 0:
                heapq.heappush(maxHeap, (prev_count, prev_char))
                
            prev_char = char
            prev_count = count
        
        if len(s) != len(res):
            return ""

        return res
            