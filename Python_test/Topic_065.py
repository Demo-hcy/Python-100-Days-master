class Persion:
    def __init__(self,Name = 'hcy',Birthday=24,High = 174 ,Wight= 140):
        self.name = Name
        self.birthday = Birthday
        self.high = High
        self.wight = Wight


    def WeightRange(self):
        # high = input('请输入身高')
        if self.wight > 130:
            print('体重超过最高标')
        elif self.wight  < 110:
            print('体重超过最低标')

    def HightRange(self):
        # high = input('请输入身高')
        if self.high > 130:
            print('身高超过最高标')
        elif self.high  < 110:
            print('身高超过最低标')

if __name__ == '__main__':
    Persion = Persion()
    Persion.name = 'hcy'
    Persion.Birthday = 24
    print("姓名为：",Persion.name,"年龄为：",Persion.Birthday)
    Persion.WeightRange()
    Persion.HightRange()


