#!/usr/bin/env python3

def main():
    with open('input.txt', 'r') as file:
        trees = [line.rstrip() for line in file.readlines()]

    height = len(trees)
    width = len(trees[0])

    x, y = 0, 0
    r = 0
    while y < height:
        if trees[y][x] == '#':
            r += 1
        x = (x + 3) % width
        y += 1

    print(r)


if __name__ == '__main__':
    main()
