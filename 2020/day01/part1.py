#!/usr/bin/env python3

def main():
    with open('input.txt', 'r') as file:
        nums = [int(line) for line in file.readlines()]

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == 2020:
                print(nums[i] * nums[j])
                return


if __name__ == '__main__':
    main()
