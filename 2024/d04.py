import pathlib


def a():
    grid = pathlib.Path("d04.in").read_text().splitlines()
    height = len(grid)
    width, = {len(gridline) for gridline in grid}
    strokes = [
        *[
            # up-to-down
            [(x, y+n) for n in range(4)]
            for x in range(width)
            for y in range(height - 3)
        ],
        *[
            # bottom-to-up
            [(x, y-n) for n in range(4)]
            for x in range(width)
            for y in range(3, height)
        ],
        *[
            # left-to-right
            [(x+n, y) for n in range(4)]
            for x in range(width - 3)
            for y in range(height)
        ],
        *[
            # right-to-left
            [(x-n, y) for n in range(4)]
            for x in range(3, width)
            for y in range(height)
        ],
        *[
            # NW-to-SE
            [(x+n, y+n) for n in range(4)]
            for x in range(width - 3)
            for y in range(height - 3)
        ],
        *[
            # SE-to-NW
            [(x-n, y-n) for n in range(4)]
            for x in range(3, width)
            for y in range(3, height)
        ],
        *[
            # NE-to-SW
            [(x-n, y+n) for n in range(4)]
            for x in range(3, width)
            for y in range(height - 3)
        ],
        *[
            # SW-to-NE
            [(x+n, y-n) for n in range(4)]
            for x in range(width - 3)
            for y in range(3, height)
        ],
    ]


    return sum(
        1
        for stroke in strokes
        if [grid[x][y] for x, y in stroke] == ["X", "M", "A", "S"]
    )


if __name__ == "__main__":
    print(a())
