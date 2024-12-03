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


if __name__ == "__main__":
    print(a())
