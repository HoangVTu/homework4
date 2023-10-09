def allcaps(txt):
    def wrapper():
        result = txt()
        result = txt().upper()
        print([result])
    return wrapper