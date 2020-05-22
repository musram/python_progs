class Solution:

    def countSquares(self, matrix):
        print(self.count_one(matrix) +  self.count_more_than_one(matrix))

    def count_one(self, matrix):
       return sum( [ 1 for row in matrix for col in row if col == 1] )


    def count_more_than_one(self, matrix):

        m = len(matrix)
        n  = len(matrix[0])

        c = 0


        while m >1 and n >1:
            for i in range(m-1):
                for j in range(n-1):
                    if matrix[i][j] == 0 or matrix[i][j+1] == 0 or matrix[i+1][j] ==  0 or matrix[i+1][j+1] == 0:
                        matrix[i][j] = 0
                    else:
                        c += 1
            m -= 1
            n -= 1
                    
        return c
      
        
    
        



if __name__ == "__main__":
    matrix = [
        [0,1,1,1],
        [1,1,1,1],
        [0,1,1,1]
    ]

    matrix = [
        [1,0,1],
        [1,1,0],
        [1,1,0]
        ]

    sol  = Solution()
    sol.countSquares(matrix)
        
