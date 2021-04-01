class A:
    def who(self):
        print('A', end='\n')

class B(A):
    def who(self):
        super(B, self).who()
        print('B', end='\n')

class C(A):
    def who(self):
        super(C, self).who()
        print('C', end='\n')

class D(B, C):
    def who(self):
        super(D, self).who()
        print('D', end='\n')

item = D()
item.who()