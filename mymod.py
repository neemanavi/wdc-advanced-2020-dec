import random

x = 100

y = [10, 20, 30]

z = {'a': 1, 'b': 2, 'c': 3}


def hello(name):
    return f'Hello, {name}!'


if __name__ == '__main__':
    for i in range(5):
        print(f'Welcome to {__name__}!')
        print(random.randint(0, 10))
