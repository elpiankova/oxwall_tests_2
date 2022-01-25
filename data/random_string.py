import random
import string


def random_string(minlen=1, maxlen=255):
    length = random.randint(minlen, maxlen)
    symbols = (string.ascii_letters + string.digits + string.punctuation + " "*10)
    result = ''.join(random.choices(symbols, k=length))
    return result


def random_string(minlen=1, maxlen=256, spaces=False, whitespases=False, enter=False, cyr=False):
    length = random.randint(minlen, maxlen)
    symbols = string.ascii_letters + string.digits + string.punctuation
    if spaces:
        symbols += ' ' * 10
    if whitespases:
        symbols += string.whitespace[:-2] * 3
    if enter:
        symbols += "\n"*3
    if cyr:
        cyr_symbol = ''.join([chr(l) for l in range(0x0400, 0x04FF)
                              if chr(l).isprintable()])
        symbols += cyr_symbol
    result = ''.join(random.choices(symbols, k=length))
    return result


if __name__ == '__main__':
    print(string.punctuation)
    print(string.ascii_letters)
    print(string.printable)

    print(random.randint(0, 100))
    print(100 * random.random())
    print(random.choice([34, 0, 6, "a"]))
    print(random.choices([34, 0, 6, "a"], k=10))

