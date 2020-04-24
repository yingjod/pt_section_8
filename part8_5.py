def print_(string):
    '''

    check the string length and print it out by different way

    '''
    if len(string)==6:
        print('|%-10s|'%(string))
        print('|%s|'%string.center(10))
        print('|%10s|'%string)

if __name__ == '__main__':
    string = input()
    print_(string)