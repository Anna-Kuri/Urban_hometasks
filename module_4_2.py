def test_function():
    print ("Test function")
    def inner_function():
        print("I am in the scope of the test_function function")
    inner_function()

test_function()

inner_function()

