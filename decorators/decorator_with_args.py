def func_decorator(original_func):
    def wrapper(*args):  # this wraps the original function
        print("I'd like to add a star")
        original_func(*args)
        print("A new star exists")

    return wrapper


@func_decorator  # syntactic sugar for "tree = func_decorator(tree)"
def tree(color):
    print(f"I'm a {color} tree")


if __name__ == "__main__":
    tree("green")
