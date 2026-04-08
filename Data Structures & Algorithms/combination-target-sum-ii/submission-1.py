class Solution:
    def combinationSum2(self, cd: List[int], target: int) -> List[List[int]]:
        
        resList = list()
        
        def solve(idx,target,combination,resList):
            # print(idx,cd[idx])
            if target == 0:
                if sorted(combination) not in resList:
                    resList.append(list(sorted(combination)))
                    # print("resList = ",resList)
                return
            if idx >= len(cd):
                return
            if target <0:
                return
            
            
            # Take cd[idx]
            combination.append(cd[idx])
            solve(idx+1,target-cd[idx],combination,resList)
            combination.pop()
            solve(idx+1,target,combination,resList)

        solve(0,target,[],resList)
        return resList
        
