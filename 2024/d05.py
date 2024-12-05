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


def a():
    rules, updates = load_file()
    return sum(
        update[len(update) // 2]
        for update in updates
        if is_correctly_ordered(rules, update)
    )


if __name__ == "__main__":
    print(a())
