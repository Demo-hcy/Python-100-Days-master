def TestTry(index,flag = False):
    stulst =['abc','def','ghk']
    if flag:
        try:
            astu = stulst[index]
        except IndexError:
            print('IndexError')
        return 'Try Test Finish'
    else:
        astu = stulst[index]
        return ' NO Try Test Finish'

if __name__ == '__main__':
    print('Try Test start.......')
    print(TestTry(1,True))
    print(TestTry(1, False))
    print(TestTry(4,True))
    print(TestTry(4, False))
