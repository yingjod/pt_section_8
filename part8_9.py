def check_(pw):

    """
    
    check the password is valid or not

    """
    valipw = True

    if len(pw) <= 7 or pw.isalpha() or pw.islower() or pw.isdigit():
        valipw = False

    else:
        for i in range(0, len(pw)):
            if not pw[i].isalpha() and not pw[i].isdigit():
                valipw = False
                break
    return valipw


if __name__ == "__main__":
    pw = input()
    answer = check_(pw)
    if answer:
        print("valid password")

    else:
        print("invalid password")
