class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=[]
        for i,a in enumerate(nums):
            if a>0:
                break   
            if i>0 and nums[i-1]==nums[i]:
                continue         
            l=i+1
            r=len(nums)-1
            while l<r:
                currsum=a+nums[l]+nums[r]
                if currsum==0:
                    ans.append([a,nums[l],nums[r]]) 
                    l+=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
                elif currsum>0:
                    r-=1
                else:
                    l+=1
        return ans