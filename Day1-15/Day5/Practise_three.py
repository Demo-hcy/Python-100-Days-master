from random import randint


class CRAPS:
    def Gambling(self):
        global Pbet, Carry_on
        money =1000
        while money > 0:
            if money> 0:
                print('你的总资产为:', money)
                Carry_on =False
                while True:
                    Pbet =int(input("请下注"))
                    if 0< Pbet <=money:
                        break
            else:
                print("你已经没有钱了")

            First = randint(1,6) +randint(1,6)
            print("摇的点数",First)
            if First ==7 or First == 11:
                money+= (Pbet*2)
                print("玩家赢,你的总资产变为：",money)
            elif First == 2 or First ==3 or First== 12 :
                money-=Pbet
                print("庄家赢，你还剩：",money)
            else:
                Carry_on = True

            while Carry_on:
                Carry_on=False
                Second = randint(1,6) + randint(1,6)
                print("摇的点数",Second)
                if Second == 7:
                    money -= Pbet
                    print("庄家赢，你还剩：",money)
                elif Second == First:
                    money += (Pbet * 2)
                    print("玩家赢,你的总资产变为：", money)
                else:
                    Carry_on = True
if __name__ == '__main__':
    CR = CRAPS()
    GB = CR.Gambling()