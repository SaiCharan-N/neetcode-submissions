class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result=[]
        def backtracking(op,cl,s):
            if len(s)==2*n:
                result.append(s)
            if op<n:
                backtracking(op+1,cl,s+'(')
            if cl<op:
                backtracking(op,cl+1,s+')')
        backtracking(0,0,"")
        return result