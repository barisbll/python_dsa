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
    assert sum_of_digits(945) == 18, "Error"
    assert sum_of_digits(5) == 5, "Error"
    assert sum_of_digits(729) == 18, "Error"
    assert sum_of_digits(729987) == 42, "Error"
    assert sum_of_digits(10) == 1, "Error"
    assert sum_of_digits(29.3) == "Input n is invalid", "Error"
    assert sum_of_digits(-4) == "Input n is invalid", "Error"


if __name__ == "__main__":
    main()
