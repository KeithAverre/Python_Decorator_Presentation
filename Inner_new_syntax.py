def new_function(func):
    def new_funct():
        print("new feature")
    def another_funct():
        print("another cool feature")

    new_funct()
    func("french_toast")
    another_funct()

@new_function
def original_function(msg):
    print(f'This is original function with a message: {msg}')

