def func_decorator(original_func):
    def wrapper():  # this wraps the original function
        print("I'd like to add a star")
        original_func()
        print("A new star exists")

    return wrapper


@func_decorator  # syntactic sugar for "tree = func_decorator(tree)"
def tree():
    print("I'm a tree")


if __name__ == "__main__":
    tree()
