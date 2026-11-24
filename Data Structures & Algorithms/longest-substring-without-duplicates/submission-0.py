class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic={}
        l=0
        ans=0
        for r in range(len(s)):
            if s[r] in dic:
                while s[l]!=s[r]:
                    del dic[s[l]]
                    l+=1
                l+=1
            else:
                dic[s[r]]=1
            ans=max(ans,r-l+1)
        return ans 
