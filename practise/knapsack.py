__author__ = 'lol'
# val = (60, 100)
# wt = (10, 20)
# W = 50
cache = {}
val = (60, 100, 120, 432,543,324,56,32,32324,42,3252,60, 100, 120, 432,543,324,56,32,32324,42,3252,60, 100, 120, 432,543,324,56,32,32324,42,3252,60, 100, 120, 432,543,324,56,32,32324,42,325)
wt = (10,20,30,434,34,23,235,324,5,243,324,10,20,30,434,34,23,235,324,5,243,324,60, 100, 120, 432,543,324,56,32,32324,42,3252,60, 100, 120, 432,543,324,56,32,32324,42,325)
W = 9100

def knapsack(W, val, wt, i):
    if W == 0 or i == 0:
        return 0
    if wt[i-1] > W:
        return knapsack(W, val, wt, i-1)
    key = (W, val, wt, i)
    if key not in cache:
        cache[key] = max(knapsack(W, val, wt, i-1), val[i-1] + knapsack(W - wt[i-1], val, wt, i-1))
    return cache[key]

print knapsack(W, val, wt, len(wt))