class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def helper(opened,total,st):
            if len(st) == 2*n:
                res.append(st)
                return
            if opened > 0:
                helper(opened-1,total+1,st + '(')
            
            if total > 0:
                helper(opened,total-1,st+')')
        helper(n,0,"")
        return res
            