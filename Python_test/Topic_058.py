class PrntA:    # 父类A
    namea = 'PrntA'
    def A_SetValue(self,a):
        self.a = a

    def A_Set_numberA(self,numberA):
        PrntA.numberA = numberA

    def info(self):
        print('PrntA:%s,%s' % (PrntA.namea, self.a))

class PrntB:
    nameb = 'PrntB'
    def B_Set_numberB(self,numberB):
        PrntB.numberB = numberB

    def info(self):
        print('PrntB:%s' % (PrntB.nameb))

class Sum1(PrntA, PrntB):
    pass
class Sum2(PrntB, PrntA):
    pass

class Sum3(PrntA, PrntB):
    def info(self):
        PrntA.info(self)
        PrntB.info(self)

if __name__ == '__main__':
    print('第一个类')
    sum1 = Sum1()
    sum1.A_SetValue('111111')
    sum1.info()
    sum1.B_Set_numberB('①①①①①①①①')
    sum1.info()
    print('第二个类')
    sum2 = Sum2()
    sum2.A_SetValue('2222222')
    sum2.info()
    sum2.B_Set_numberB('②②②②②②②')
    sum2.info()
    print('第三个类')
    sum3 = Sum3()
    sum3.A_SetValue('3333333')
    sum3.info()
    sum3.B_Set_numberB('③③③③③③③③')
    sum3.info()
