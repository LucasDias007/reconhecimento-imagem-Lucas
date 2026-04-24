def is_prime(number: int) -> bool:
    """
    Check if a given integer is a prime number.

    A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

    Args:
        number (int): The integer to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False

    # Check for factors up to sqrt(number)
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6

    return True

if __name__ == "__main__":
    test_cases = [1, 2, 3, 4, 17, 18, 19, 20]
    for value in test_cases:
        result = is_prime(value)
        print(f"{value} -> {result}")
