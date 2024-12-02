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


def is_dampened_safe(level):
    if is_safe(level):
        return True

    return any(
        is_safe(level[:idx] + level[idx + 1:])
        for idx in range(0, len(level))
    )


def a():
    with open("d02.in") as fp:
        return sum(
            1
            for level_desc in fp
            if is_safe(list(map(int, level_desc.split())))
        )


def b():
    with open("d02.in") as fp:
        return sum(
            1
            for level_desc in fp
            if is_dampened_safe(list(map(int, level_desc.split())))
        )



if __name__ == "__main__":
    print(a())
    print(b())
