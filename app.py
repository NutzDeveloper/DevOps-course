import pytest

def add(a, b):
        return (a+b)
def test_add():
        assert add(2,2) == 5

test_add()
