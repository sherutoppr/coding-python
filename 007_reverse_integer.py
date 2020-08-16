'''
Given a 32-bit signed integer, reverse digits of an integer.
'''


def reverse(x: int) -> int:
    sign = 1
    if x < 0:
        sign = -1
        x = str(x)[1:]
    else:
        x = str(x)

    x = int(str(x)[::-1])
    return 0 if x > 2 ** 31 else sign * x


print(reverse(-120))   # -21
