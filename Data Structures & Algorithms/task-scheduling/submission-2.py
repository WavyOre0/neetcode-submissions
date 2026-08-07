class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hmap = Counter(tasks)

        maxHeap = []
        for count in hmap.values():
            heapq.heappush(maxHeap, -count) # negative value because it need to be maxHeap.
        # need a queue to keep track of the time the char can be used again
        q = deque()
        time = 0
        while maxHeap or q:
            time += 1
            if maxHeap:
                count = 1 + heapq.heappop(maxHeap) # keep track of new count
                if count:
                    q.append((count, time + n))
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time
                
        