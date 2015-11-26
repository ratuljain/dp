# # # Enter your code here. Read input from STDIN. Print output to STDOUT
# # ip = [int(i) for i in raw_input().split()]
# # N = ip[0]  ### sum
# # M = ip[1]    ##number of coins
# coins = tuple([int(i) for i in raw_input().split()])
cache = {}
def change(N, coins):
    global cache
    if N == 0:
        return 1
    if len(coins) == 0 and N > 0 or N < 0:
        return 0
    key = (N, len(coins))
    if key in cache:
        return cache[key]
    cache[key] = change(N, coins[:-1]) + change(N - coins[-1], coins)
    return cache[key]



N = 4

coins = (1,2,3)
print change(N, coins)