def factorial(n):
    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


def sum_digits(n):
    if n < 10:
        return n

    return n % 10 + sum_digits(n // 10)


def reverse_string(s):
    if len(s) <= 1:
        return s

    return s[-1] + reverse_string(s[:-1])


def power(base, exp):
    if exp == 0:
        return 1

    return base * power(base, exp - 1)
