class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hmap = Counter(tasks)

        maxHeap = []
        for count in hmap.values():
            heapq.heappush(maxHeap, -count)
        time = 0
        q = deque()
        while maxHeap or q:
            time += 1
            if maxHeap:
                count = 1 + heapq.heappop(maxHeap)
                if count != 0:
                    q.append((count, time + n))
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time

        
            