class Countdown(object):
    def __init__(self, step):
        self.step = step

    def next(self):
        if self.step == 0:
            raise StopIteration
        self.step -= 1
        return self.step

    def __iter__(self):
        """Returns iterator"""
        return self


def countdown_example():
    for el in Countdown(4):
        print(el)


def fibonacci():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b


def fibonacci_example():
    fib = fibonacci()
    print(fib.__next__())
    print(fib.__next__())
    print([fib.__next__() for i in range(0)])


def generator():
    try:
        yield 'something'
    except ValueError:
        yield 'exception'
    finally:
        print('the end')


def generator_example():
    gen = generator()
    print(gen.__next__())
    gen.throw(ValueError('aaa'))
    gen.close()
