# 在Python中，我们可以将那些在运行时可能会出现状况的代码放在`try`代码块中，
# 在`try`代码块的后面可以跟上一个或多个`except`来捕获可能出现的异常状况。
# 例如在上面读取文件的过程中，文件找不到会引发`FileNotFoundError`，
# 指定了未知的编码会引发`LookupError`，
# 而如果读取文件时无法按指定方式解码会引发`UnicodeDecodeError`，
# 我们在`try`后面跟上了三个`except`分别处理这三种不同的异常状况。
# 最后我们使用`finally`代码块来关闭打开的文件，释放掉程序中获取的外部资源


def main():
    f = None
    try:
        f = open('C:\\Users\\zrwjh\\Desktop\\测试.txt', 'r', encoding='utf-8')
        print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件!')
    except LookupError:
        print('指定了未知的编码!')
    except UnicodeDecodeError:
        print('读取文件时解码错误!')
    finally:
        if f:
            f.close()


if __name__ == '__main__':
    main()