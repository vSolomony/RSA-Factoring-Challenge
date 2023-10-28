#!/usr/bin/python3
import sys
import sympy


def factorize(n):
    factors = sympy.factorint(n)
    return factors


def main(filename):
    try:
        with open(filename, "r") as file:
            n = int(file.read().strip())
            factors = factorize(n)
            for prime, exponent in factors.items():
                print(f"{prime}^{exponent}", end=" ")
            print()
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except ValueError:
        print("Invalid input in the file.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python prime_factors.py <file>")
    else:
        filename = sys.argv[1]
        main(filename)
