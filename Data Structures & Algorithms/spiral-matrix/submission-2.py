class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left=0
        right=len(matrix[0])
        top=0
        bot=len(matrix)
        result=[]
        while left < right and top < bot:
            for col in range(left, right):
                result.append(matrix[top][col])
            top+=1
            for row in range(top,bot):
                result.append(matrix[row][right-1])
            right-=1
            if not (left < right and top < bot):
                break
            for col in range(right-1,left-1,-1):
                result.append(matrix[bot-1][col])
            bot-=1
            for row in range(bot-1,top-1,-1):
                result.append(matrix[row][left])
            left+=1
        return result


