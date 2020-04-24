def check_(lst):
    """

    if the word start from 'B' will add in list

    """
    while True:
        str = input()
        if str != "end":
            if str.startswith("B"):
                lst.append(str)
        else:
            break

    print(lst)


if __name__ == "__main__":
    lst = []
    check_(lst)
