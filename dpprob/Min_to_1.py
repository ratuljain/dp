__author__ = 'lol'


def _min(n):

    if n <= 1:
        return 0
    if n % 3 == 0:
            x = _min(n // 3)
    if n % 3 == 0:
            y = _min(n // 2)

    z = _min(n - 1)

    return 1 + (min(x , y, z))


print min(16)
print min(1,2,3)