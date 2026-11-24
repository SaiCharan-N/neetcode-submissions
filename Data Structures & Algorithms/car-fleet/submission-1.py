class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if not position:
            return 0
        ans=1
        dic={}
        n=len(position)
        for i in range(n):
            dic[position[i]]=speed[i]
        position.sort()
        pointer=n-1
        for i in range(n-2,-1,-1):
            t1=(target-position[i])/dic[position[i]]
            t2=(target-position[pointer])/dic[position[pointer]]
            if t1<=t2:
                pass
            else:
                ans+=1
                pointer=i
        return ans

