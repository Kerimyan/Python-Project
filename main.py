## timer decorator
def timeer_decorator(fn):
    from datetime import datetime
    from functools import wraps

    @wraps(fn)
    def inner(*args, **kwargs):
        start = datetime.now()
        result = fn(*args,**kwargs)
        stop = datetime.now()
        elapsed = stop - start

        print(f'{fn.__name__} run for {elapsed}s::')

        return result
    return inner

