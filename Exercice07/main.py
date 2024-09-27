# Écrivez votre code ici !
def square(number: int | float) -> int | float:
    """Square a number

    Args:
        number (int | float): The number to square

    Returns:
        int | float: The square of the number
    Raises:
        TypeError: If the number is not an int or float
    """
    if not isinstance(number, (int, float)):
        raise TypeError(f"Error: {type(number)} is not an int or float")
    return number * number


s = square("8")
print(s)
