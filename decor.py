#The most basic decorator

def Yell(func):
    def wrapper():
        
        func_original = func()
        func_decorated = func_original.upper()

        return func_decorated
    return wrapper

@Yell
def HelloWorld():
    return 'hello world'

result = HelloWorld()
print(result)
    
