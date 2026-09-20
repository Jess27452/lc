class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows=len(matrix)
        cols=len(matrix[0])
        top=0
        bottom=rows-1
        while top<=bottom:
            middle=top+(bottom-top)//2
            if target>matrix[middle][-1]:
                top=middle+1
            elif target<matrix[middle][0]:
                bottom=middle-1
            else:
                break
        if top>bottom:
            return False
        left=0
        right=cols-1
        row=top+(bottom-top)//2
        while left<=right:
            middle=left+(right-left)//2
            if matrix[row][middle] < target:
                left=middle+1
            elif matrix[row][middle]==target:
                return True
            else:
                right=middle-1
        return False

