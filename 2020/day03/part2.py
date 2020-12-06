#!/usr/bin/env python3

def main():
    with open('input.txt', 'r') as file:
        trees = [line.rstrip() for line in file.readlines()]

    height = len(trees)
    width = len(trees[0])

    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    r = 1
    for slope in slopes:
        x, y = 0, 0
        t = 0
        while y < height:
            if trees[y][x] == '#':
                t += 1
            x = (x + slope[0]) % width
            y += slope[1]
        r *= t

    print(r)


if __name__ == '__main__':
    main()
