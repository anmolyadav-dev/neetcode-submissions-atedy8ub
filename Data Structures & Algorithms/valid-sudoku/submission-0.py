class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        len = 9
        rowHashSet= [set() for i in range(9)]
        colHashSet= [set() for i in range(9)]

        gridHashSet= {}

        for i in range(9):
            for j in range(9):
                val=board[i][j]
                if(val != "."):
                    key = (i//3 , j//3)
                    if val in rowHashSet[i] or val in colHashSet[j]: return False;
                    rowHashSet[i].add(val)
                    colHashSet[j].add(val)
                    if key not in gridHashSet:
                        gridHashSet[key]=set()
                    if val in gridHashSet[key]:return False
                    gridHashSet[key].add(val)

        # print(rowHashSet)
        # print("\n")
        # print(colHashSet)
        # print("\n")
        # print(gridHashSet)
        return True



        