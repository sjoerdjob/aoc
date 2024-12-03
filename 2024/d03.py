import pathlib
import re


def a():
    return sum(
        int(match["multiplier"]) * int(match["multiplicant"])
        for match in re.finditer(
            r"mul\((?P<multiplier>[0-9]+),(?P<multiplicant>[0-9]+)\)",
            pathlib.Path("d03.in").read_text(),
        )
    )


def b():
    mul_on = True
    total = 0
    for match in re.finditer(
        "|".join(
            [
                r"(mul)\((?P<multiplier>[0-9]+),(?P<multiplicant>[0-9]+)\)",
                r"(do|don't)\(\)",
            ]
        ),
        pathlib.Path("d03.in").read_text(),
    ):
        if match[4] == "don't":
            mul_on = False
        if match[4] == "do":
            mul_on = True
        if mul_on and match[1] == "mul":
            total += int(match["multiplier"]) * int(match["multiplicant"])
    return total

if __name__ == "__main__":
    print(a())
    print(b())
