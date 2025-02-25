def cap(func):
    def wrepper():
        result = func()
        return result.upper()
    return wrepper

@cap
def greet():
    return "hello world!!"

print(greet())