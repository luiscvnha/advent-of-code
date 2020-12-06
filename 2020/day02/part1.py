#!/usr/bin/env python3

def parse(lines):
    r = []
    for line in lines:
        l0, passwd = line.split(': ')
        l1, letter = l0.split(' ')
        low, high = l1.split('-')
        r.append((int(low), int(high), letter, passwd))
    return r


def main():
    with open('input.txt', 'r') as file:
        passwds = parse(file.readlines())

    r = 0
    for elem in passwds:
        c = 0
        for char in elem[3]:
            if char == elem[2]:
                c += 1
        if elem[0] <= c <= elem[1]:
            r += 1

    print(r)


if __name__ == '__main__':
    main()
