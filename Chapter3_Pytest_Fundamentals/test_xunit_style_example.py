def setup_module(module):
    print("\nSetting up module - This will be executed once for each test file")


def teardown_module(module):
    print("\nTeardown  module - This will be executed once for each test file")


def setup_function(function):
    if function == test_1:
        print("\nSetting up test1!")
    elif function == test_2:
        print("\nSetting up test2!")
    else:
        print("nSetting up uknown test!")


def teardown_function(function):
    if function == test_1:
        print("\nTearing down test1!")
    elif function == test_2:
        print("\nTearing down up test2!")
    else:
        print("Tearing down uknown test!")


def test_1():
    print("Executing test1")
    assert True


def test_2():
    print("Executing test2")
    assert True
