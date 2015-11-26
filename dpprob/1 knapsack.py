__author__ = 'lol'
val = (60, 100, 120, 432,543,324,56,32,32324,42,3252,60, 100, 120, 432,543,324,56,32,32324,42,3252,60, 100, 120, 432,543,324,56,32,32324,42,3252,60, 100, 120, 432,543,324,56,32,32324,42,325)
weight = (10,20,30,434,34,23,235,324,5,243,324,10,20,30,434,34,23,235,324,5,243,324,60, 100, 120, 432,543,324,56,32,32324,42,3252,60, 100, 120, 432,543,324,56,32,32324,42,325)
capacity = 9100
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
def knapsack(capacity, val, weight):
    if capacity <= 0 or len(val) <= 0:
        return 0
    if weight[-1] > capacity:
        return knapsack(capacity, val[:-1], weight[:-1])
    return max((val[-1] + knapsack(capacity-weight[-1], val[:-1], weight[:-1])), knapsack(capacity, val[:-1], weight[:-1]))

print knapsack(capacity, val, weight)



