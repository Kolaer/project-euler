from typing import Iterator


def fibonacci_generator() -> Iterator[int]:
    a, b = 1, 2

    while True:
        yield a
        a, b = b, a + b


def even_fibonacci_generator() -> Iterator[int]:
    a, b = 2, 8

    while True:
        yield a
        a, b = b, 4 * b + a


def solve(n: int) -> int:
    fib_sum = 0
    fib_iter = fibonacci_generator()

    while True:
        fib_number = next(fib_iter)

        if fib_number > n:
            break
        elif fib_number % 2 != 0:
            continue

        fib_sum += fib_number

    return fib_sum


def no_check_solve(n: int) -> int:
    fib_sum = 0
    fib_iter = fibonacci_generator()
    next(fib_iter)

    while True:
        fib_number = next(fib_iter)

        if fib_number > n:
            break

        fib_sum += fib_number

        next(fib_iter)
        next(fib_iter)

    return fib_sum


def even_iter_solve(n: int) -> int:
    fib_sum = 0
    fib_iter = even_fibonacci_generator()

    while True:
        fib_number = next(fib_iter)

        if fib_number > n:
            break

        fib_sum += fib_number

    return fib_sum


if __name__ == "__main__":
    n = 4_000_000

    print(solve(n))
    print(no_check_solve(n))
    print(even_iter_solve(n))
