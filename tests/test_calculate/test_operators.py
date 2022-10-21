from pytest_learning.calculate.operators import Operators


def test_should_make_multiple_addition():
    sut = Operators()
    operation = "5.5 + 10 + 30 + 13.7"
    expected_value = 59.2
    assert sut.addition(operation) == expected_value


def test_should_make_multiple_substraction():
    sut = Operators()
    operation = "15 - 5 - 2"
    expected_value = 8
    assert sut.substraction(operation) == expected_value


def test_should_make_multiplication():
    sut = Operators()
    operation = "5 * 2"
    expected_value = 10
    assert sut.multiplication(operation) == expected_value


def test_should_make_division():
    sut = Operators()
    operation = "8 / 2"
    expected_value = 4
    assert sut.division(operation) == expected_value
