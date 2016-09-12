def example1():
    a = [i for i in range(10) if i % 2 == 0]


def example2_part1(pos, element):
    return '%d: %s' % (pos, element)


def example2_part2():
    seq = ["one", "two", "three"]
    a = [example2_part1(i, el) for i, el in enumerate(seq)]
