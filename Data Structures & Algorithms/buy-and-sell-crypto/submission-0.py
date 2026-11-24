class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans=0
        m=prices[0]
        for c in prices:
            v=c-m
            if ans<v:
                ans=v
            if c<m:
                m=c
        return ans