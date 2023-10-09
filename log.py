import time

def timestamp(txt):
    def wrapper():
        print(time.ctime())
        txt()
    return wrapper