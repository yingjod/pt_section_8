
def compute(sentence,word):
    '''

    to count how many times word show in the sentence

    '''
    return sentence.count(word)

if __name__ == '__main__':
    sentence=input()
    word=input()
    count=compute(sentence,word)
    print(word,'occurs',count,'time(s)')
