def log_decorator(func):
    def wrapper(*args, **kwargs):
        print("====================")
        print("Avant la fonction !")
        print("====================")
        result = func(*args, **kwargs)
        print("====================")
        print("Après la fonction :)")
        print("====================")
        return result

    return wrapper


@log_decorator
def function_test():
    print("Cette fonction ne prend pas d'arguments.")


function_test()
