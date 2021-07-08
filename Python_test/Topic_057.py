class Ant:

    #定构造方法
    def __init__(self,x=0,y=0,color ='black'):
        self.x = x
        self.y = y
        self.color = color

    #定义运动距离方式
    def Distance(self):
        print('当前位置：(%d,%d)'%(self.x,self.y))

    #定义爬行方式
    def Exercise_mode(self,x,y):
        self.x =x
        self.y =y
        print('爬行')
        self.Distance()

    #定义行为
    def Behavior(self):
        print('发射')

class Ant_son(Ant):
    # 定义飞行方式
    def FLY(self, x, y):
        print('飞行')
        self.x = x
        self.y = y
        self.Distance()

    # 定义行为
    def Behavior(self):
        print('攻击')

class Son(Ant):
    def Swiming(self,x,y):
        print('游泳')
        self.x =x
        self.y =y
        self.Distance()


if __name__ == '__main__':
    ant_son = Ant_son(color='red')
    ant_son.Exercise_mode(3,5)
    ant_son.FLY(1,10)
    ant_son.Behavior()
    son= Son()
    son.Swiming(2,5)
