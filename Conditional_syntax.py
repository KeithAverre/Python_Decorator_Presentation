def new_function(selector):
    def inner_funct(func):
        def new_funct():
            print("new feature")
        def another_funct():
            print("another cool feature")
        new_funct()
        if(selector == 1):
            func("french_toast")
        else:
            func("waffles")
        another_funct()
    return inner_funct # this is a must

@new_function(int(input("please pick a number\n")))
def original_function(msg):
    print(f'This is original function with a message: {msg}')