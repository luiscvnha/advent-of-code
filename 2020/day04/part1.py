#!/usr/bin/env python3

import re


def main():
    with open('input.txt', 'r') as file:
        r = [len(re.findall(r'(byr|iyr|eyr|hgt|hcl|ecl|pid):', p)) for p in file.read().split('\n\n')].count(7)

    print(r)


if __name__ == '__main__':
    main()
