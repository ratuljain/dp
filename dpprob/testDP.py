def LowestCommonSubstring(s1, s2):
    LCS = [[0 for x in range(len(s2) + 1)] for x in range(len(s1) + 1)]
    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):
            if s1[i - 1] == s2[j - 1]:
                LCS[i][j] = 1 + LCS[i-1][j-1]
            else:
                LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])
    return LCS[i][j]


cache = {}
from functools import wraps

def memo(func):
    cache = {}
    @wraps(func)
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap
@memo
def lcs(xstr, ystr):
    if not xstr or not ystr:
        return ""
    x, xs, y, ys = xstr[0], xstr[1:], ystr[0], ystr[1:]
    if x == y:
        return x+ " " + lcs(xs, ys)
    else:
        return max(lcs(xstr, ys), lcs(xs, ystr), key=len)

s1 = "16 27 89 79 60 76 24 88 55 94 57 42 56 74 24 95 55 33 69 29 14 7 94 41 8 71 12 15 43 3 23 49 84 78 73 63 5 46 98 26 40 76 41 89 24 20 68 14 88 26"
s2 = "27 76 88 0 55 99 94 70 34 42 31 47 56 74 69 46 93 88 89 7 94 41 68 37 8 71 57 15 43 89 43 3 23 35 49 38 84 98 47 89 73 24 20 14 88 75"
l1 = tuple(s1.split(" "))
l2 = tuple(s2.split(" "))
print lcs(l1, l2)
