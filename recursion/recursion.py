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
def GCD(n1, n2):
    pass


def main():
    # factorial tests
    assert factorial(5) == 120, "Error"
    assert factorial(1) == 1, "Error"
    assert factorial(6) == 720, "Error"
    assert factorial(-5) == "Input n is invalid", "Error"
    assert factorial(0.5) == "Input n is invalid", "Error"

    # fibonacci tests
    assert fibonacci(0) == 0, "Error"
    assert fibonacci(1) == 1, "Error"
    assert fibonacci(2) == 1, "Error"
    assert fibonacci(3) == 2, "Error"
    assert fibonacci(5) == 5, "Error"
    assert fibonacci(7) == 13, "Error"
    assert fibonacci(29.3) == "Input n is invalid", "Error"
    assert fibonacci(-4) == "Input n is invalid", "Error"

    # sum of digits test
    assert sum_of_digits_alternative(945) == 18, "Error"
    assert sum_of_digits_alternative(5) == 5, "Error"
    assert sum_of_digits_alternative(729) == 18, "Error"
    assert sum_of_digits_alternative(729987) == 42, "Error"
    assert sum_of_digits_alternative(10) == 1, "Error"
    assert sum_of_digits_alternative(29.3) == "Input n is invalid", "Error"
    assert sum_of_digits_alternative(-4) == "Input n is invalid", "Error"

    # power of n tests
    assert power_of_n(2, 3) == 8, "Error"
    assert power_of_n(5, 3) == 125, "Error"
    assert power_of_n(17, 2) == 289, "Error"
    assert power_of_n(9, 3) == 729, "Error"
    assert power_of_n(29.3, 1/2) == "Input n is invalid", "Error"
    assert power_of_n(-4, -4) == "Input n is invalid", "Error"


if __name__ == "__main__":
    main()
