class TestClass:
    test_var = "This is a test class."
    
    def test_method(self):
        print("This is a test method inside TestClass.")
        print("self refers to the instance of the class.")
        print(self.test_var)

test = TestClass()
print(test.test_var)
print(test.test_method())

    