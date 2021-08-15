import time

def time_it(func):
    '''
    This decorator is to time the execution of any function
    '''
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()

        print(func.__name__ + " took " + str((end-start)*1000) + " ml sec")
        return result
    return wrapper