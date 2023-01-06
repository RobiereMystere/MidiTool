DEBUG = False


def log(*args):
    if DEBUG:
        print(args)


def print_dict(data):
    string = ""
    prefix = "\t"
    for key, value in data.items():
        string += str(key) + " = "
        if type(value) is dict:
            for k, v in value.items():
                if v is not None:
                    string += str(k) + " = "
                    string += prefix * 2 + str(v) + "\n"
        else:
            string += prefix + str(value) + "\n"

    print(string)
