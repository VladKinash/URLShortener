
def Base62_encoder(number):
    Base62 = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    shortened = []

    if number == 0:
        return Base62[0]
    
    while number != 0:

        number, remainder = divmod(number, 62)
        shortened.append(Base62[remainder])

    return ''.join(reversed(shortened))
