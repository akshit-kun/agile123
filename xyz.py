"""Simple program to add two numbers."""


def add_numbers(first_number, second_number):
    """Return the sum of two numbers."""
    return first_number + second_number


def main():
    """Main function."""
    result = add_numbers(2, 3)
    print(result)


if __name__ == "__main__":
    main()