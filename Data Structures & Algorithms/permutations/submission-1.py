class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.result=[]
        n=len(nums)
        used=[False]*n
        def backtrack(index,a,u):
            if len(a)==n:
                self.result.append(a)
            if len(a)>n:
                return 
            for i in range(n):
                if u[i]==False:
                    u[i]=True
                    backtrack(index+1,a+[nums[i]],u)
                    u[i]=False
        backtrack(0,[],used)
        return self.result