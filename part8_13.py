import random


def change_(str):
    """
    
    get ten random number between 65~90 and transform to alphabet

    """
    for i in range(1, 11):
        randnum = random.randint(65, 90)
        str += chr(randnum)
    return str


if __name__ == "__main__":
    str = ""
    a = change_(str)
    print(a)
