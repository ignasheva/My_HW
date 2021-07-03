def parse_args(*args):
    start, stop, step = None, None, None
    if len(args) == 1:
        start, stop, step = None, args[0], None
    elif len(args) == 2:
        start, stop, step = args[0], args[1], None
    elif len(args) == 3:
        start, stop, step = args[0], args[1], args[2]
    return start, stop, step


def custom_range(source, *args):
    params = []
    for arg in args:
        params.append(source.find(arg) if type(arg) is not int else arg)
    start, stop, step = parse_args(*params)
    return list(source[start:stop:step])
