__author__ = 'lol'
cost = ((1, 7, 9, 2 ),
        (8, 6, 3, 2),
        (1, 6, 7, 8 ),
        (2, 9, 8, 2))
cost = tuple(cost)

cache = {}
def minCost(m, n, cost):
    global cache
    key = (m, n, len(cost))
    if key in cache:
        return cache[key]
    if m < 0 or n < 0:
        return 0
    if m == 0 and n == 0:
        return cost[m][n]
    cache[key] = cost[m][n] + min( minCost(m, n-1, cost), minCost(m-1, n, cost))
    print cache
    return cache[key]

class Solution:
    def minCost(self, m, n, grid):
        dp = [[0 for i in xrange(n)] for i in xrange(m)]
        dp[0][0] = grid[0][0]

        for i in xrange(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]

        for j in xrange(1, n):
            dp[0][j] = dp[0][j - 1] + grid[0][j]

        for i in xrange(1, m):
            for j in xrange(1, n):
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]

    def minPathSum(self, grid):
        m, n = len(grid), len(grid[0])
        return self.minCost(m, n, grid)

    def maxSubArraySum(self, a):
        if sum(number for number in a if number < 0) == sum(a):
            return max(a)
        size = len(a)
        max_so_far = 0
        max_ending_here = 0

        for i in range(0, size):
            max_ending_here = max_ending_here + a[i]
            if max_ending_here < 0:
                max_ending_here = 0

            if (max_so_far < max_ending_here):
                max_so_far = max_ending_here

        return max_so_far

s = Solution()
l = [-2, -3, -1, -5]
print sum(number for number in l if number < 0)
# print max(l)
print s.maxSubArraySum(l)