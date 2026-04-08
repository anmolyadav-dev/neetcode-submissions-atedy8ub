class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        op = {'+' , '-' , '*' , '/'}
        for i in tokens:

            if i not in op:
                st.append(int(i))
            else:
                sec = int(st[-1])
                st.pop()
                fir = int(st[-1])
                st.pop()
                if i == '+':
                    st.append(fir + sec)
                elif i == '*':
                    st.append(fir*sec)
                elif i == '/':
                    st.append(int(fir/sec))
                else :
                    st.append(fir-sec) 
        return st[-1]

        