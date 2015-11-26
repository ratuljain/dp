__author__ = 'lol'
N = 4
coins = [1,2,3]

def change(N, coins):
    if N == 0:
        return 1
    if N < 0:
        return 0
    if len(coins) == 0 and N > 0:
        return 0
    return change(N, coins[:-1]) + change(N-coins[-1], coins)

print change(N, coins)