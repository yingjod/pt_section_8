def slipit(s):
    '''

    split the string and print out the average and total

    '''
    slist=[int(x) for x in s.split(' ')]

    print('total=', sum(slist))
    print('average=', sum(slist) / len(slist))

if __name__ == '__main__':
    s = input()
    slipit(s)

