"""main example file."""

from package_test import package_test


def main():
    """Main example function."""
    number = package_test.add_one(1)
    print(number)


if __name__ == "__main__":
    main()
