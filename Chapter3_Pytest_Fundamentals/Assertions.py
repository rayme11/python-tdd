import pytest


@pytest.fixture()
def setup():
    print("\nSetup texture")


def test1(setup):
    print("nExecuting test1!")


@pytest.mark.usefixtures("setup")  # same result as test1
def test2():
    print("nExecuting test2!")
    assert {"1": 1} == {"1": 1}
