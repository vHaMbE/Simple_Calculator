import pytest
import sys
import calculator


def test_calculator_sum():
    sum = calculator.add_multiple(2, 4, 7, 5)
    assert sum == 18


def test_calculator_product():
    product = calculator.multiply_multiple(2, 6, 3)
    assert product == 36
