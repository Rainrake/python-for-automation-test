import pytest

@pytest.fixture ()
def some_test(some_number):
    return some_number
@pytest.fixture ()
def some_number():
    return 5

def test_some3(some_test):
    assert  some_test == 5
