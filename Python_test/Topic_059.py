x = 3
class A:
    def __init__(self,v=5):
        self.v = v

class B:
    def __init__(self):
        self.a = A()
    def chng(self,x,y):
        self.info()
        x = 0
        self.a.v =0
        self.info()
    def info(self):
        print(x,self.a.v)

if __name__ == '__main__':
    b = B()
    b.chng(0,0)