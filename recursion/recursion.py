from decimal import Decimal


# Write a recursive function that takes factorial of a given number
def factorial(n):
    if n < 0 or not isinstance(n, int):
        return "Input n is invalid"

    if n in [0, 1]:
        return 1
    else:
        return n * factorial(n - 1)


# Write a recursive function that takes a number and finds fibonacci sum of the number
def fibonacci(n):
    if n < 0 or not isinstance(n, int):
        return "Input n is invalid"

    if n in [0, 1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


# How to find the sum of digits using recursion?
def sum_of_digits(n):

    if n < 0 or not isinstance(n, int):
        return "Input n is invalid"

    # to avoid floating point errors
    n = Decimal(n)
    if n / 10 < 1.0:
        return n
    else:
        remainder = ((n/10) % 1) * 10
        return remainder + sum_of_digits(int(n/10))


def sum_of_digits_alternative(n):
    if n < 0 or not isinstance(n, int):
        return "Input n is invalid"

    if n == 0:
        return 0
    else:
        return int(n % 10) + sum_of_digits_alternative(int(n/10))


# How to calculate power of a number using recursion
def power_of_n(n, p):
    if p < 0 or not isinstance(p, int):
        return "Input n is invalid"

    if p == 0:
        return 1
    else:
        return n * power_of_n(n, p-1)


# How to find GCD (Greatest Common Divisor) of two numbers using recursion
def gcd(n1, n2, counter=1, temp_gcd=1):
    if n1 <= 0 or n2 <= 0 or not isinstance(n1, int) or not isinstance(n2, int):
        return "Input n is invalid"

    if (min(n1, n2) < counter):
        return temp_gcd
    else:
        if ((n1 / counter) % 1 == 0) and ((n2 / counter) % 1 == 0):
            return gcd(n1, n2, counter + 1, counter)
        else:
            return gcd(n1, n2, counter + 1, temp_gcd)

# Find GCD of two numbers using recursion


def gcd_euclidian(a, b):
    if int(a) != a or int(b) != b:
        return "Input n is invalid"

    if a < 0:
        a = -1 * a
    if b < 0:
        b = -1 * b

    if b == 0:
        return a
    else:
        return gcd(b, a)


def main():
    # factorial tests
    # assert factorial(5) == 120, "Error"
    # assert factorial(1) == 1, "Error"
    # assert factorial(6) == 720, "Error"
    # assert factorial(-5) == "Input n is invalid", "Error"
    # assert factorial(0.5) == "Input n is invalid", "Error"

    # fibonacci tests
    # assert fibonacci(0) == 0, "Error"
    # assert fibonacci(1) == 1, "Error"
    # assert fibonacci(2) == 1, "Error"
    # assert fibonacci(3) == 2, "Error"
    # assert fibonacci(5) == 5, "Error"
    # assert fibonacci(7) == 13, "Error"
    # assert fibonacci(29.3) == "Input n is invalid", "Error"
    # assert fibonacci(-4) == "Input n is invalid", "Error"

    # sum of digits test
    # assert sum_of_digits_alternative(945) == 18, "Error"
    # assert sum_of_digits_alternative(5) == 5, "Error"
    # assert sum_of_digits_alternative(729) == 18, "Error"
    # assert sum_of_digits_alternative(729987) == 42, "Error"
    # assert sum_of_digits_alternative(10) == 1, "Error"
    # assert sum_of_digits_alternative(29.3) == "Input n is invalid", "Error"
    # assert sum_of_digits_alternative(-4) == "Input n is invalid", "Error"

    # power of n tests
    # assert power_of_n(2, 3) == 8, "Error"
    # assert power_of_n(5, 3) == 125, "Error"
    # assert power_of_n(17, 2) == 289, "Error"
    # assert power_of_n(9, 3) == 729, "Error"
    # assert power_of_n(29.3, 1/2) == "Input n is invalid", "Error"
    # assert power_of_n(-4, -4) == "Input n is invalid", "Error"

    # GCD tests
    assert gcd_euclidian(10, 15) == 5, "Error"
    assert gcd_euclidian(55, 77) == 11, "Error"
    assert gcd_euclidian(89, 22) == 1, "Error"
    assert gcd_euclidian(-16, 52) == 4, "Error"
    assert gcd_euclidian(16, 0.5) == "Input n is invalid", "Error"
    assert gcd_euclidian(16, 0.8) == "Input n is invalid", "Error"


if __name__ == "__main__":
    main()
