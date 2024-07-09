import time
import random


#
# Credits: https://calmcode.io/course/decorators/behavior We've seen how functions can accept functions in python as
# input. Let's use this knowledge to create a function that accepts a function as input but also returns a function
# as output.
#
def stopwatch(f):
    def func():
        tic = time.time()
        result = f()
        print(f"this function took: {time.time() - tic}")
        return result

    return func


def sleep_random():
    time.sleep(random.random())
    return "Done!"


timed_sleep = stopwatch(sleep_random)
