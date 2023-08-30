import pytest


@pytest.fixture()
def setup():
    print("\nSetup texture")


def test1_feature(setup):
    print("nExecuting test1 - feature testing!")


@pytest.mark.usefixtures("setup")  # same result as test1
def test2_regression():
    print("nExecuting test2 - regression testing!")
    assert {"1": 1} == {"1": 1}
