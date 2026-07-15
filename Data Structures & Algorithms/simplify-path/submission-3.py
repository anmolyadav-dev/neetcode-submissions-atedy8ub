class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        i = 0
        while i<len(path):
        
            if path[i]=='/':
                if not stack:
                    stack.append('/')
                if stack and stack[-1]!= '/':
                    stack.append('/')
                while i<len(path) and path[i]=='/': i+=1

            elif i<len(path) and path[i]=='.':
                ct=1;
                i+=1
                # print(i,ct)
                while i<len(path) and path[i]==".":
                    ct+=1
                    i+=1
                print(i,ct)
                if  (i<len(path) and path[i]=="/") or i >= len(path):
                    
                    if ct>=3:
                        stack.append("."*ct)
                    if ct == 2:
                        if stack:
                            stack.pop()
                        if stack:
                            stack.pop()
                else:
                    stack.append("."*ct)
            else:
                temp = ""
                while i<len(path) and (path[i]!= "/"):
                    temp+=path[i]
                    i+=1
                print("temp: ",temp)
                x=""
                if "." in stack[-1]:
                    x = stack.pop()
                stack.append(x+temp)
        res = []
        if len(stack)>1 and stack[-1] == '/':
            stack.pop()
        while stack:
            res.append(stack.pop())
        return "".join(res[::-1])
        