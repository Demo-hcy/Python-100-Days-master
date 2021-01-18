import os
import time


def Text():
    content = '高宏是小仙女----'

    while True:
        os.system("cls")
        print(content)
        time.sleep(0.2)
        content = content[1:] + content[0]

if __name__ == '__main__':
    Text()
