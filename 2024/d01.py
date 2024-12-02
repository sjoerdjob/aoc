import pathlib


def lists():
    with open("d01.in") as fp:
        pairs = [
            tuple(map(int, line.split()))
            for line in fp
        ]
    left, right = map(list, zip(*pairs))
    return left, right


def a():
    left, right = lists()
    left.sort()
    right.sort()
    return sum(
        abs(l - r)
        for l, r in zip(left, right)
    )


def b():
    left, right = lists()
    return sum(
        l * right.count(l)
        for l in left
    )


if __name__ == "__main__":
    print(a())
    print(b())
