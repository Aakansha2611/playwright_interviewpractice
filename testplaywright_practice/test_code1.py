import pytest

@pytest.fixture(scope = "function")
def prework():
    print("pre-work")
    return "fail"

@pytest.fixture(scope = "function")
def secondwork():
    print("secondwork 1")
    yield
    print("secondwork 2")


def test_check(prework,secondwork) :
    print("akansha2")
    assert prework == "fail"


def test_checkpresetupwork(presetupwork) :
    print("akansha verifying conftest" )

@pytest.mark.skip
def test_checkskip(presetupwork) :
    print("akansha verifying skip" )

