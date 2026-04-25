def calculate_statistics(numbers: list[int]) -> tuple[int, float, int, int]:
    """
    Calculate total, average, maximum, and minimum of a list of numbers.

    Args:
        numbers (list[int]): List of integers.

    Returns:
        tuple: (total, average, maximum, minimum)
    """
    if not numbers:
        raise ValueError("List cannot be empty")
    
    total = sum(numbers)
    average = total / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    
    return total, average, maximum, minimum

if __name__ == "__main__":
    numbers = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]
    total, average, maximum, minimum = calculate_statistics(numbers)
    print("total:", total)
    print("media:", average)
    print("maior:", maximum)
    print("menor:", minimum)