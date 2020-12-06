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
        if (elem[3][elem[0]-1] == elem[2]) != (elem[3][elem[1]-1] == elem[2]):
            r += 1

    print(r)


if __name__ == '__main__':
    main()
