__author__ = 'mark'

def multiple(m, n):
    if n == 1:
        return m
    k = multiple(m, n / 2)
    if n%2 == 1:
        return 2*k + m
    else:
        return 2*k

print multiple(2, 5)
