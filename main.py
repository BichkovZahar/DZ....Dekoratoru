import time
def delay_decorator(func):
    def wrapper(*args , **kwargs):
        time.sleep(1.5)
        return func(*args , **kwargs)
    return wrapper

@delay_decorator
def sleepy():
    print('Hello!')
for i in range(3):
    sleepy()