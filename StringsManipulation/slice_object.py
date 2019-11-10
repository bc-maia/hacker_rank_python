string = ['a','b','c','d','e','f','g']

if __name__ == "__main__":
    obj = slice(None, None, 2)

    print(string[obj])

    print(string[::2])