import time
import random

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