import sys


def factorize(n):
    factors = {}
    divisor = 2
    while n > 1:
        if n % divisor == 0:
            if divisor not in factors:
                factors[divisor] = 1
            else:
                factors[divisor] += 1
            n //= divisor
        else:
            divisor += 1
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

