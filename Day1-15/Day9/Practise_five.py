# 继承
#
# 刚才我们提到了，可以在已有类的基础上创建新类，这其中的一种做法就是让一个类从另一个类那里将属性和方法直接继承下来，
# 从而减少重复代码的编写。提供继承信息的我们称之为父类，也叫超类或基类；
# 得到继承信息的我们称之为子类，也叫派生类或衍生类。子类除了继承父类提供的属性和方法，还可以定义自己特有的属性和方法，
# 所以子类比父类拥有的更多的能力，在实际开发中，我们经常会用子类对象去替换掉一个父类对象，这是面向对象编程中一个常见的行为，
# 对应的原则称之为[里氏替换原则]

class Person(object):
    """人"""

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        print('%s正在愉快的玩耍.' % self._name)

    def watch_av(self):
        if self._age >= 18:
            print('%s正在观看搞笑电影.' % self._name)
        else:
            print('%s只能观看《熊出没》.' % self._name)



class Student(Person):
    """学生"""

    def __init__(self,name ,age , grade):
        super().__init__(name ,age)
        self._grade =grade
    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade

    def study(self, course):
        print('%s的%s正在学习%s.' % (self._grade, self._name, course))


class Teacher(Person):
    """老师"""

    def __init__(self,name, age, title):
        super().__init__(name, age)
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    def teach(self, course):
        print('%s%s正在讲%s.' % (self._name, self._title, course))


def main():
    stu = Student('小红', 20, '初中生')
    stu.study('数学')
    stu.watch_av()
    stu.age = 15
    stu.watch_av()
    stu.grade = '高中生'
    stu.study('生物')
    t = Teacher('老王', 38, '专家')
    t.teach('高等数学')
    t.watch_av()
    t.age = 15
    t.watch_av()


if __name__ == '__main__':
    main()
