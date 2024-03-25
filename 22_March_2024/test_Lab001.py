import pytest

def test_substraction():
    assert 2-2 == 0

@pytest.mark.smoke
def test_multi():
    assert 2*2 == 4

@pytest.mark.reg
def test_add():
    assert 2+2 == 4

@pytest.mark.reg
def test_add2():
    assert 2+32 == 34

@pytest.mark.skip(reason = "Not implimented yet")
def test_multi():
    assert 2*2 == 42