def A(x,y):
    return(abs(x),abs(y))

class B:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
        self.F()

    def C(self,x,y):
        x,y = A(x,y)
        self.D(x,y)
        self.F()

    def D(self,x,y):
        self.x +=x
        self.y +=y

    def F(self):
        print('当前位置为（%d,%d）'%(self.x,self.y))

if __name__ == '__main__':
    b = B()
    b.C(3,4)
    b.C(-1,9)
