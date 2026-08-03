## *args  -- allowes multiple argument - used when how many arguments to pass


def values(*args):  # it can be any parameter with starting with *
    print(*args)
    print(type(args))  # but *args is standard form of writing


values(10, 20)
