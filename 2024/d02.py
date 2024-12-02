def is_safe(level):
    if (
        level != sorted(level)
        and level != sorted(level, reverse=True)
    ):
        return False

    return all(
        1 <= abs(a - b) <= 3
        for a, b in zip(level[:-1], level[1:])
    )


def a():
    with open("d02.in") as fp:
        return sum(
            1
            for level_desc in fp
            if is_safe(list(map(int, level_desc.split())))
        )


if __name__ == "__main__":
    print(a())
