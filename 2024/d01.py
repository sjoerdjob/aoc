import pathlib


def a():
    with open("d01.in") as fp:
        pairs = [
            tuple(map(int, line.split()))
            for line in fp
        ]
    left, right = map(list, zip(*pairs))
    left.sort()
    right.sort()
    return sum(
        abs(l - r)
        for l, r in zip(left, right)
    )


if __name__ == "__main__":
    print(a())
