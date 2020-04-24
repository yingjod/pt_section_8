def look_(str, fstr):
    """

    to search fstr in str or not,and use "Bright" instead of the fstr and print it

    """
    if str.find(fstr) != -1:
        endstr = str.replace(fstr, "Bright")
        print(endstr)
    else:
        print(fstr + "is not found ")


if __name__ == "__main__":
    str = input()
    fstr = input()
    look_(str, fstr)
