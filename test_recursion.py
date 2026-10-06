from recursion import factorial, sum_digits, reverse_string, power


def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(4) == 24
    assert factorial(5) == 120


def test_sum_digits():
    assert sum_digits(5) == 5
    assert sum_digits(12) == 3
    assert sum_digits(472) == 13
    assert sum_digits(999) == 27


def test_reverse_string():
    assert reverse_string("") == ""
    assert reverse_string("a") == "a"
    assert reverse_string("cat") == "tac"
    assert reverse_string("hello") == "olleh"


def test_power():
    assert power(2, 0) == 1
    assert power(2, 3) == 8
    assert power(5, 2) == 25
    assert power(3, 4) == 81
