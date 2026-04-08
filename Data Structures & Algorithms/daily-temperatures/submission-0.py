class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        res = [0]*len(temperatures)
        for i in range(len(temperatures)):
            if not st:
                st.append(i)
            else:
                while st and  temperatures[st[-1]] < temperatures[i]:
                    x = st.pop()
                    res[x] = i - x
                st.append(i)
        
        while st :
            x = st.pop()
            res[x] = 0
        
        return res

        