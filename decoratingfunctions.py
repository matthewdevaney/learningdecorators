# decorators can do something before or after a function
def before_and_after(function):
    def wrapper():
        txt = 'before'
        txt2 = function()
        txt3 = 'after'
        return '\n'.join((txt, txt2, txt3))
    return wrapper


@before_and_after
def middle():
    return 'middle'


print(middle())


# they can add something to a number
def plus_one(function):
    def wrapper():
        x = function()
        return x + 1
    return wrapper()


@plus_one
def function_call():
    return 5


print(function_call)


# they can capitalize a text string
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper


# and they can be stacked
@uppercase_decorator
@before_and_after
def say_hi():
    return 'hello there'


print(say_hi())


def decorator_with_arguments(function):
    def wrapper(*args, **kwargs):
        txt = function(*args, **kwargs)
        print('The positional arguments are', args)
        print('The keyword arguments are', kwargs)
    return wrapper


@decorator_with_arguments
def function_with_no_arguments(my_arg, keyword_arg=None):
    print(f"{my_arg} and {keyword_arg}.")


function_with_no_arguments('Yesyesyesyes', keyword_arg='Nononono')


"""main pattern for creating a decorator

import functools

def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        value = func(*args, **kwargs)
        # Do something after
        return value
    return wrapper_decorator
"""

"""
time how long something takes to execute


import functools
import time

def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer

@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])
"""

"""
slow down some code

import functools
import time

def slow_down(func):
    @functools.wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)
    return wrapper_slow_down

@slow_down
def countdown(from_number):
    if from_number < 1:
        print("Liftoff!")
    else:
        print(from_number)
        countdown(from_number - 1)
"""

"""
debug your code
import functools

def debug(func):
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]                      # 1
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # 2
        signature = ", ".join(args_repr + kwargs_repr)           # 3
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")           # 4
        return value
    return wrapper_debug
"""