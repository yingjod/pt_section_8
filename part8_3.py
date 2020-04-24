def splitit(string):
    '''

   print out last three words in string

    '''
    s_list=string.split(' ')
    print(' '.join(s_list[-3:]))

if __name__ == '__main__':
    string = input()
    splitit(string)
