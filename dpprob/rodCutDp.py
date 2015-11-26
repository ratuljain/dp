__author__ = 'lol'
price = [0, 1, 5, 8, 9, 10]

def profit(length, price):
    if length in [1,2,3,4,5]:
        return 1
    else:

        piece = 1 + profit(length - 2 , price)
        return piece

print profit(6, price)