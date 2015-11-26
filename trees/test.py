# class Solution:
# # @param obstacleGrid, a list of lists of integers
# # @return an integer
#     def uniquePathsWithObstacles(self, obstacleGrid):
#         m = len(obstacleGrid)
#         n = len(obstacleGrid[0])
#         print m, n
#         ResGrid = [[0 for x in range(n+1)] for x in range(m+1)]
#         ResGrid[0][1] = 1
#         print ResGrid
#
#         for i in range(1, m+1):
#             for j in range(1, n+1):
#                 if not obstacleGrid[i-1][j-1]:
#                     ResGrid[i][j] = ResGrid[i][j-1]+ResGrid[i-1][j]
#
#         return ResGrid[m][n]

x = [[ 1, 7, 9, 2 ],
     [ 8, 6, 3, 2 ],
     [ 1, 6, 7, 8 ],
     [ 2, 9, 8, 2 ]]
pri
x = tuple([tuple(i) for i in x])
z = [[1, 7, 9, 2]]
print x
from functools import wraps
import math
# res, l = [], []
cache = {}
class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def memo(func):
        cache = {}
        @wraps(func)
        def wrap(*args):
            if args not in cache:
                cache[args] = func(*args)
            return cache[args]
        return wrap
    @memo
    def minCostPath(self, grid, m, n):
        # global cache
        key = (grid, m, n)
        if m == 0 and n == 0:
            return  grid[m][n]
        if m == 0:
            return  grid[0][n] + self.minCostPath(grid,  m, n-1)
        if n == 0:
            return  grid[m][0] + self.minCostPath(grid,  m-1, n)
        if m > 0 and n > 0:
            return  grid[m][n] + min(self.minCostPath(grid,  m-1, n), self.minCostPath(grid,  m, n-1))

    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        obstacleGrid[0][0] = 1 - obstacleGrid[0][0]

        for i in range(1, n):
            if not obstacleGrid[0][i]:
                obstacleGrid[0][i] = obstacleGrid[0][i-1]
            else:
                obstacleGrid[0][i] = 0

        for i in range(1, m):
            if not obstacleGrid[i][0]:
                obstacleGrid[i][0] = obstacleGrid[i-1][0]
            else:
                obstacleGrid[i][0] = 0
        print obstacleGrid
        for i in range(1, m):
            for j in range(1, n):
                if not obstacleGrid[i][j]:
                    obstacleGrid[i][j] = obstacleGrid[i][j-1]+obstacleGrid[i-1][j]
                else:
                    obstacleGrid[i][j] = 0

        return obstacleGrid

    def numSquares(self, n):
        n = int(math.sqrt(n))
        l = range(1, n+1)
        print l,n
        return self.helper(n, l)

    def helper(self, n, l):
        global res
        if n < 0:
            return 0
        if n == 1:
            return 1
        return min()



cdict = {}


def C(i, coins):
    if i == 0:
        return 0

    if i < 0:
        return 01e100  # Return infinity in ideally

    if i in cdict:
        return cdict[i]
    else:
        answer = 1 + min([C(i - cj * cj, coins) for cj in coins])
        cdict[i] = answer
    return answer



s = Solution()
# x =[
#   [0,0,0],
#   [1,1,1],
#   [0,0,0]
# ]
# print s.uniquePathsWithObstacles(x)
print s.minCostPath(x, 3, 3)

