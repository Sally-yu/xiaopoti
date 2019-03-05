from functools import reduce
import re


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1


def main():
    b = 'yuzhaoyang'
    b.replace('y', 'Y')
    print()


def aa(s):
    return 'aa' + s


def bb(s):
    return 'bb' + s


def ab(a, b, s):
    return a(s) + b(s)


def add(x, y):
    sum = 1


if __name__ == '__main__':
    main()
    f = fib(6)
    for n in f:
        print(n)
    print(lambda x: 'aa'+x, lambda x: 'bc'+x, 'oooooo')
    print(sum({1, 2, 3, 4, 5}))
    print([a + b + c for a in 'abcd'.upper()
           for b in '1234' for c in 'XYZ'.upper()])
    s = r'^\d{3}\-\d{3,8}$'
    ss = '222-434'
    a = '1 b  3,;;;   gfds; s d,  d'
    print(re.match(s, ss))
    print(re.split(r'[\s\,\;]+', a))
