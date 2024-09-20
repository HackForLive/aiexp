def calculate(operation: str, x: int, y: int) -> int:
    """
    operation takes the string (add, sub, mul, div)
    x & y
    """
    if operation == 'Addition':
        return x + y
    elif operation == 'Subtraction':
        return x - y
    elif operation == 'Multiplication':
        return x*y
    elif operation == 'Division':
        return x/y
    else:
        raise NotImplementedError("Unknown operation")
