
def check(s):
    '''

    check the s is all correct format

    '''
    isSNN=(len(s)==11)
    if isSNN:
        for i in range(len(s)):
            if i ==3 or i ==6:
                if s[i]!='-':
                    isSNN=False
                    break
            elif not s[i].isdigit():
                isSNN=False
                break
        return isSNN

if __name__ == '__main__':
    s = input()
    isSNN=check(s)
    if isSNN:
        print('valid SSN')
    else:
        print('Invalid SSN')