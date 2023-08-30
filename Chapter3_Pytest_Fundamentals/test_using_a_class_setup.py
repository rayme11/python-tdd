class TestClass:
    @classmethod
    def setup_class(cls):
        print("Setup TestClass - This will be executed once for each test class")

    @classmethod
    def teardown_class(cls):
        print("\nTeardown  module - This will be executed once for each test class")

    def setup_method(self, method):
        if method == self.test_1():
            print("\nSetting up test1!")
        elif method == self.test_2():
            print("\nSetting up test2!")
        else:
            print("\nSetting up uknown test!")

    def teardown_method(self, method):
        if method == self.test_1:
            print("\nTearing down test1!")
        elif method == self.test_2:
            print("\nTearing down up test2!")
        else:
            print("\nTearing down uknown test!")

    def test_1(self):
        print("Executing test1")
        assert True

    def test_2(self):
        print("Executing test2")
        assert True
