def sum_of_multiples(up_to: int, multiple: int) -> int:
    number_of_multiples = up_to // multiple
    reduced_sum_of_mulpiles = (number_of_multiples * (number_of_multiples + 1)) // 2

    return multiple * reduced_sum_of_mulpiles


def solve(n: int) -> int:
    return sum_of_multiples(n, 3) + sum_of_multiples(n, 5) - sum_of_multiples(n, 15)


if __name__ == "__main__":
    n = 1_000

    print(solve(n))
