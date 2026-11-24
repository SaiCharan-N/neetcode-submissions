class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        ans=-float('inf')
        while l<r:
            area=min(heights[l],heights[r])*(r-l)
            if area>ans:
                ans=area
            if heights[l]>heights[r]:
                r-=1
            else:
                l+=1
        return ans 
