class Demo:
    class_name = 'Demo_Name'  # 类变量

    def __init__(self,x=0):   # 实例变量
        self.x = x

    def class_info(self):
        print('类变量:',Demo.class_name)
        print('实例变量：',self.x)

    def change_x(self,x):
        self.x = x

    def change_name(self,name):
        Demo.class_name = name

if __name__ == '__main__':
    demo1 = Demo()
    demo2 = Demo()
    print('初始两个实例')
    demo1.class_info()
    demo2.class_info()
    print('修改实例变量')
    print('修改demo1的实例变量')
    demo1.change_x(3)
    demo1.class_info()
    demo2.class_info()
    print('------------------')
    print('修改demo2的实例变量')
    demo2.change_x(5)
    demo1.class_info()
    demo2.class_info()
    print('------------------')
    print('修改类变量')
    print('修改demo1的类变量')
    demo1.change_name('demo1_name')
    demo1.class_info()
    demo2.class_info()
    print('------------------')
    print('修改demo2的类变量')
    demo1.change_name('demo2_name')
    demo1.class_info()
    demo2.class_info()
    print('------------------')


