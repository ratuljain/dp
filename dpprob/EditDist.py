__author__ = 'lol'
cache = {}

def editDistance(s1, s2):
    global cache
    if len(s1) == 0:
        return len(s2)
    if len(s2) == 0:
        return len(s1)
    key = (len(s1), len(s2))
    if key in cache:
        return cache[key]
    diff = 0 if s1[-1] == s2[-1] else 1
    a = editDistance(s1[:-1], s2[:-1]) + diff
    b = 1 + editDistance(s1[:-1], s2)
    c = 1 + editDistance(s1, s2[:-1])
    cache[key] = min(a, b, c)
    return cache[key]

print cache
print editDistance("AGGTAB", "GXTXAYB")
