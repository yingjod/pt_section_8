def make_(lst):
    """
    
    to get nine numbers from user

    """
    for i in range(1, 10):
        str = input()
        lst.append(str)
    return lst


def print_(lst):
    """
    
    print list out

    """
    for k in range(1, 10):
        if k % 3 != 0:
            print("|" + lst[k - 1].center(15) + "|", end="")
        else:
            print("|" + lst[k - 1].center(15) + "|")


if __name__ == "__main__":
    lst = []
    make_(lst)
    print_(lst)
