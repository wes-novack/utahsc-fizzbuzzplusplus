import src.main as main
import pytest


fizzbuzz_test_data = [
    (1, "1"),
    (2, "2"),
    (3, "fizz"),
    (4, "4"),
    (5, "buzz"),
    (6, "fizz"),
    (15, "fizzbuzz"),
    (9, "fizz"),
    (10, "buzz"),
    (30, "fizzbuzz")
]

@pytest.mark.parametrize("number, result", fizzbuzz_test_data)
def test_fizzbuzz(number, result):
    assert main.fizzbuzz(number) == result
