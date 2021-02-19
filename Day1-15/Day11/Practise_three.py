# 由于`finally`块的代码不论程序正常还是异常都会执行到（
# 甚至是调用了`sys`模块的`exit`函数退出Python环境，`finally`块都会被执行，
# 因为`exit`函数实质上是引发了`SystemExit`异常），
# 因此我们通常把`finally`块称为“总是执行代码块”，
# 它最适合用来做释放外部资源的操作。
# 如果不愿意在`finally`代码块中关闭文件对象释放资源，
# 也可以使用上下文语法，通过`with`关键字指定文件对象的上下文环境并在离开上下文环境时自动释放文件资源

def main():
    try:
        with open('C:\\Users\\zrwjh\\Desktop\\测试.txt', 'r', encoding='utf-8') as f:
            print(f.read())


    except FileNotFoundError:

        print('无法打开指定的文件!')

    except LookupError:

        print('指定了未知的编码!')

    except UnicodeDecodeError:

        print('读取文件时解码错误!')


if __name__ == '__main__':
    main()
