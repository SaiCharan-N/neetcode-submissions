import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones=[-i for i in stones]
        heapq.heapify(stones)
        c=0
        while len(stones):
            x=heapq.heappop(stones)
            if stones:
                y=heapq.heappop(stones)
            else:
                return abs(x)
            if x==y:
                c=0
            else:
                c=abs(x-y)
                heapq.heappush(stones,-c)
        return 0
        