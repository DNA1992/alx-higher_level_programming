#!/usr/bin/python3
import sys


def main():
    sumTotal = 0
    for x in range(1, len(sys.argv)):
        sumTotal += int(sys.argv[x])
    print("{:d}".format(sumTotal))


if __name__ == "__main__":
    main()
