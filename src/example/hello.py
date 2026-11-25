"""A simple Hello World example"""

def greet(name: str = "World") -> str:
    """Return a greeting.
    
    :param name: Name of the person or entity to greet.
        Defaults to "World".
    :Returns: A friendly greeting.
    """
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(greet())
