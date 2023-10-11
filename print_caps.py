def allcaps(txt):
    def wrapper():
        value = txt()
        result = value.upper()
        return(result)
    return wrapper