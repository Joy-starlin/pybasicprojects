"""A small demo library of Python functions and their usage."""


def add_numbers(a, b):
    """Return the sum of two numbers.

    Args:
        a: First number.
        b: Second number.
    """
    return a + b


def describe_person(name, age=18, city="Unknown"):
    """Demonstrate default arguments and keyword usage."""
    return f"{name} is {age} years old and lives in {city}."


def find_first_even(numbers):
    """Return the first even number or None if none is found."""
    for number in numbers:
        if number % 2 == 0:
            return number
    return None


def collect_words(*words):
    """Demonstrate *args by collecting positional arguments."""
    return list(words)


def build_profile(**info):
    """Demonstrate **kwargs by building a profile dictionary."""
    return {"profile": info}


def outer_scope_example(value):
    """Show how a local variable is separate from an outer scope."""
    local_value = value + 1
    return local_value


def fibonacci(n):
    """Return the n-th Fibonacci number using recursion."""
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def factorial_recursive(n):
    """Return factorial using a recursive approach and early return."""
    if n < 0:
        return None
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)


if __name__ == "__main__":
    print("Demo: functionLibrary.py")
    print("add_numbers(4, 7) =>", add_numbers(4, 7))
    print("describe_person('Ana', city='Tokyo') =>", describe_person('Ana', city='Tokyo'))
    print("find_first_even([1, 3, 5, 8, 9]) =>", find_first_even([1, 3, 5, 8, 9]))
    print("collect_words('one', 'two', 'three') =>", collect_words('one', 'two', 'three'))
    print("build_profile(name='Sam', role='Developer') =>", build_profile(name='Sam', role='Developer'))
    print("outer_scope_example(5) =>", outer_scope_example(5))
    print("fibonacci(6) =>", fibonacci(6))
    print("factorial_recursive(5) =>", factorial_recursive(5))
