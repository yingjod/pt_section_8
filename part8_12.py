def check_(lst):
    while True:
        str = input()
        if str != "end":
            lst = str.split()
            print(lst)
        else:
            break


if __name__ == "__main__":
    lst = []
    check_(lst)
