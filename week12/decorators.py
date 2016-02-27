import datetime
import time
from functools import wraps


def accepts(*string):
    def function(func):
        @wraps(func)
        def check_type(*func_args):
            count = 0
            while count < len(func_args):
                if isinstance(func_args[count], string[count]):
                    count += 1
                else:
                    raise TypeError("Argument {} of say_hello is not {}!".\
                              format(count + 1, string[count].__name__))
            return func(*func_args)
        return check_type
    return function


@accepts(str)
def say_hello(name):
    return "Hello, I am {}".format(name)


@accepts(str, int)
def deposit(name, money):
    print("{} sends {} $!".format(name, money))
    return True


def encrypt(number):
    def function(func):
        @wraps(func)
        def cipher():
            new_string = ""
            f = func()
            for el in f:
                if el is not " ":
                    new_string += chr(ord(el) + number)
                else:
                    new_string += " "
            return new_string
        return cipher
    return function


def log(file_name):
    def function(func):
        @wraps(func)
        def save_log():
            now = datetime.datetime.now()
            with open(file_name, 'a') as f:
                f.write("{} was called at {}\n".format(func.__name__, now))
            return func()
        return save_log
    return function


@log('log.txt')
@encrypt(2)
def get_low():
    return "Get get get low"


def performance(file_name):
    def function(func):
        @wraps(func)
        def get_time():
            res = func()
            start = time.time()
            with open(file_name, 'a') as f:
                text = "{} was called and took {} seconds to complete\n".\
                        format(func.__name__, time.time() - start)
                f.write(text)
            return res
        return get_time
    return function


@performance('log_time.txt')
def something_heavy():
    time.sleep(2)
    return "I am done!"
