class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        result=[]

        for i in range(len(points)):
            distance=points[i][0]**2+points[i][1]**2
            points[i]=[distance,points[i][0],points[i][1]]
        heapq.heapify(points)
        for i in range(k):
            [a,b,c]=heapq.heappop(points)
            result.append([b,c])
        return result
