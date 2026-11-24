class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        result=[None]*len(temperatures)
        for i in range(len(temperatures)-1,-1,-1):
            if stack and temperatures[i]<stack[-1][0]:
                result[i]=stack[-1][1]-i
            else:
                while stack and  stack[-1][0]<=temperatures[i]:
                    stack.pop()
                if stack:
                    result[i]=stack[-1][1]-i
                else:
                    result[i]=0   
            stack.append([temperatures[i],i])
        return result

        