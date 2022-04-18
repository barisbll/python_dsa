# Write a recursive function that takes factorial of a given number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def main():
    # factorial tests
    assert factorial(5) == 120, "Error"
    assert factorial(1) == 1, "Error"
    assert factorial(6) == 720, "Error"


if __name__ == "__main__":
    main()
