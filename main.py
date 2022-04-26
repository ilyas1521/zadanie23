# +1 *2 2->40 v20 x8   делается все по аналогии с примером
def f(n, finish):
    if n == finish:
        return 1
    if n > finish or n == 8:
        return 0
    return f(n + 1, finish) + f(n * 2, finish)


print(f(2, 20) * f(20, 40))