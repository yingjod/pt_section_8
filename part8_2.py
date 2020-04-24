
def ord_(total,string_):
    '''

    to know every word in string ASCII and print it out

    '''
    for i in range(0,len(string_)):
        num=ord(string_[i])
        print('ASCII code for "%s" is %d'%(string_[i],num))
        total+=num

    print(total)

if __name__ == '__main__':
    total=0
    string_=input()
    ord_(total,string_)

