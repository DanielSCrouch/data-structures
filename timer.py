from functools import wraps 
from timeit import default_timer as timer

def timeit(f):
  @wraps(f)
  def wrap(*args, **kwargs):
    ts = timer()
    result = f(*args, **kwargs)
    te = timer() - ts
    # print(f'func: {f.__name__} args: [{args}, {kwargs}] took {te} sec')
    print(f'func: {f.__name__} took {te} sec')
    return result
  return wrap
