
import pytest


@pytest.fixture(scope = "function")
def presetupwork():
    print("pre-setup work")