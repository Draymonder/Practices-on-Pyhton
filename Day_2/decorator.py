

def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now(x,y):
    print(x+y)
    print('2017-10-30')

now(1,2)