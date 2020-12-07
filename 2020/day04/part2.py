#!/usr/bin/env python3

import re


def main():
    with open('input.txt', 'r') as file:
        passports = [re.findall(r'(byr|iyr|eyr|hgt|hcl|ecl|pid):(\S+)', p) for p in file.read().split('\n\n')]

    r = 0
    for p in passports:
        valid_fields = 0
        for (field, value) in p:
            if field == 'byr':
                if not 1920 <= int(value) <= 2002:
                    break
            elif field == 'iyr':
                if not 2010 <= int(value) <= 2020:
                    break
            elif field == 'eyr':
                if not 2020 <= int(value) <= 2030:
                    break
            elif field == 'hgt':
                if not (value[-2:] == 'cm' and 150 <= int(value[:-2]) <= 193
                        or
                        value[-2:] == 'in' and 59 <= int(value[:-2]) <= 76):
                    break
            elif field == 'hcl':
                if not re.match(r'^#[0-9a-f]{6}$', value):
                    break
            elif field == 'ecl':
                if value not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
                    break
            elif field == 'pid':
                if not re.match(r'^[0-9]{9}$', value):
                    break
            valid_fields += 1
        if valid_fields == 7:
            r += 1

    print(r)


if __name__ == '__main__':
    main()
