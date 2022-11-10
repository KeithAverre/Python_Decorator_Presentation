def new_function(func):
    print("new feature")
    func("french_toast")
    print("another cool feature")

def original_function(msg):
    print(f'This is original function with a message: {msg}')

new_function(original_function)

