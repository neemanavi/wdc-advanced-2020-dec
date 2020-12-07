#!/usr/bin/env python3

x = 100


def myfunc():
    x += 1
    print(f'In myfunc, x = {x}')


print(f'Before, x = {x}')
myfunc()
print(f'After, x = {x}')
