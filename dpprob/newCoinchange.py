__author__ = 'lol'
import math
from functools import wraps
class Solution(object):
    def numSquares(self, n):
            n = int(math.sqrt(n))
            l = tuple(range(1, n+1))
            return self.change(n, l)


    def memo(func):
        cache = {}
        @wraps(func)
        def wrap(*args):
            if args not in cache:
                cache[args] = func(*args)
            return cache[args]
        return wrap

    @memo
    def change(self, S, coins):
        if S is 0:
            return 1
        if not coins and S > 0:
            return 0
        if S < 0:
            return 0
        return self.change(S, coins[:-1]) + self.change(S-coins[-1], coins)
s = Solution()
print s.numSquares(1535)