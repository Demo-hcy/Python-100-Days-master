class Self_Attribute:
    def __init__(self,Weight= 140,Colour='白色',High=150,Energy=100):
        self.w =Weight
        self.c=Colour
        self.h = High
        self.e = Energy

    def Energy_Increase(self):
        self.e +=5

    def Energy_Reduction(self):
        self.e-=5

    def info(self):
        print('当前精灵的体重为：%.2f,体重为：%s,高度为：%.2fcm，能量为：%d'%(self.w,self.c,self.h,self.e))
        print()

class Behavior:
    def __init__(self):
        self.self_attribute = Self_Attribute()
    def Run(self):
        print('精灵跑步')
        self.self_attribute.Energy_Reduction()
        self.Getinfo()

    def Jump(self):
        print('精灵跳跃')
        self.self_attribute.Energy_Reduction()
        self.Getinfo()

    def Eat(self):
        print('精灵进食')
        self.self_attribute.Energy_Increase()
        self.Getinfo()

    def Getinfo(self):
        print('当前能量为：',self.self_attribute.e)

class Game:

    def __init__(self):
        self.behavior =Behavior()
        for a  in range(3):
            i = input('请选择精灵的动作：1、跑步 ，2、跳跃 ，3、进食：')
            if  i =='跑步':
                self.behavior.Run()
            elif i =='跳跃':
                self.behavior.Jump()
            elif i =='进食':
                self.behavior.Eat()
            else:
                print('当前精灵没有您输入的动作，请输入正确的动作')

if __name__ == '__main__':
    SA = Self_Attribute()
    SA.info()
    game = Game()

