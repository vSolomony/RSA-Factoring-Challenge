#!/usr/bin/python3
import sys


def factorize(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return i, n // i
    return 1, n


def main(filename):
    try:
        with open(filename, "r") as file:
            lines = file.read().splitlines()
            for line in lines:
                n = int(line)
                p, q = factorize(n)
                print(f"{n}={p}*{q}")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python factors.py <file>")
    else:
        filename = sys.argv[1]
        main(filename)
