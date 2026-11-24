class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.result=[]
        def recursion(s,a,index):
            if s==target:
                self.result.append(a)
                return 
            if s>target:
                return None
            for i in range(index,len(nums)):
                recursion(nums[i]+s,a+[nums[i]],i)
        for i in range(len(nums)):
            recursion(nums[i],[nums[i]],i)
        return self.result

