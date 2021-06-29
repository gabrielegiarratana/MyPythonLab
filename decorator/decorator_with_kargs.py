def func_decorator(original_func):
    def wrapper(*args, **kwargs):  # this wraps the original function
        print("I'd like to add a star")
        original_func(*args, **kwargs)
        print("A new star exists")

    return wrapper


@func_decorator  # syntactic sugar for "tree = func_decorator(tree)"
def tree(color):
    print(f"I'm a {color} tree")


if __name__ == "__main__":
    tree(color="green")
