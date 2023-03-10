def dummy(str, rows):
    
    if not str.isascii():
        raise Exception("Only English A to Z and '.' and ','")
    if not isinstance(rows, int):
        raise Exception("Only integers please")
    elif rows < 1 or rows >1000:
        raise Exception("Please use an integer min 1 and max 1000")

    return ""