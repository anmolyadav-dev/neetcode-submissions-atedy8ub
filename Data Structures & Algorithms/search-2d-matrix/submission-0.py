class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        l = 0
        r = m-1

        while l<=r:
            mid = l + (r-l)//2
            # print(l,r,mid)
            if matrix[mid][0] == target or matrix[mid][-1]==target:return True

            if matrix[mid][0] < target and target < matrix[mid][-1]:
                break
            
            elif matrix[mid][0] > target:
                r = mid -1;
            else:
                l = mid + 1;

        l = 0
        r = n - 1
        # print("mid")
        # print("row")
        while l<=r:
            rowmid = l + (r - l)//2
            # print(l,r,rowmid)
            if matrix[mid][rowmid] == target: return True

            if matrix[mid][rowmid] < target:
                l = rowmid+1
            else:
                r = rowmid -1
        
        return False
        
        


