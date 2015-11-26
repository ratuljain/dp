sum = 11

COINS = (1, 5, 10, 25, 50)
_change_mem = {}

def change(d, c=len(COINS), coins=COINS):
    if d == 0:
        return 1
    if d < 0 or c == 0:
        return 0

    key = (d, c, coins)
    if key not in _change_mem:
        _change_mem[key] = change(d, c - 1, coins) + change(d - coins[c - 1], c, coins)
    return _change_mem[key]

print(change(sum, 5, COINS))