class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for i in s:
            print(i,st)
            if i == '{' or i == '[' or i == '(':
                st.append(i)
            else:
                if st and ((i == '}' and st[-1]=='{') or (i== ']' and st[-1]=='[') or (i == ')' and st[-1] == '(')):
                    st.pop()
                else:
                    return False
        return False if st else True
            

        