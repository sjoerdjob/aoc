from functools import cmp_to_key, partial


def load_file():
    with open("d05.in") as fp:
        rules = []
        for line in fp:
            if not line.strip():
                break
            l, r = map(int, line.split("|"))
            rules.append((l, r))

        updates = []
        for line in fp:
            updates.append(list(map(int, line.split(","))))

    return rules, updates


def is_correctly_ordered(rules, update):
    for l, r in rules:
        try:
            if update.index(l) > update.index(r):
                return False
        except ValueError:
            continue
    return True


def compare(rules, a, b):
    for l, r in rules:
        if l == a and r == b:
            return -1
        if l == b and r == a:
            return 1
    return 0


def a():
    rules, updates = load_file()
    return sum(
        update[len(update) // 2]
        for update in updates
        if is_correctly_ordered(rules, update)
    )


def b():
    rules, updates = load_file()

    return sum(
        sorted(update, key=cmp_to_key(partial(compare, rules)))[len(update) // 2]
        for update in updates
        if not is_correctly_ordered(rules, update)
    )


if __name__ == "__main__":
    print(a())
    print(b())
