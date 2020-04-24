def print_(string):
    '''

    print out the every index from string list

    '''
    for i in range(len(string)):
        print('index of " %c ":%d'%(string[i],i))


if __name__ == '__main__':
        string = input()
        print_(string)
