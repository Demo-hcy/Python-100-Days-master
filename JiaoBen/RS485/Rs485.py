import serial
import time

def Rs485(Hex):
    # 选择串口，并设置波特率
    global return_data
    if ser.is_open:
        print("port open success")
        print("输入数据发送为：", Hex)
        send_data = bytes.fromhex(Hex)  # 数据转换
        print('发送命令,', Hex)
        print(send_data)
        ser.write(send_data)
        len_return_data = ser.inWaiting()  # 获取缓冲数据（接收数据）长度
        if len_return_data:
            return_data = ser.read(len_return_data)  # 读取缓冲数据
            print("数据返回结果为：", return_data.hex())
    else:
        print("port open failed")


def RS485_Read(Hex):
     Rs485(Hex)

def Rs485_Opened(Hex):
    Rs485(Hex)

def Rs485_Switch_Off(Hex):
    Rs485(Hex)


def Call():
    global i1_data
    for i in range(1):
            RS485_Read('01 03 00 00 00 1C 44 03')
            time.sleep(0.5)
            while i== 0:
                i1_data = return_data
                print(i1_data.hex())
                break
            if return_data == i1_data:
                print('结果一致')
            else:
                print('结果不一致')
            Rs485_Opened('01 06 00 0E 00 FF A8 49 ')
            time.sleep(0.5)
            Rs485_Switch_Off('01 06 00 0E 00 00 E8 09 ')
            time.sleep(0.5)
            print("---------------------------------")


if __name__ == '__main__':
    ser = serial.Serial("COM9", 9600)
    call = Call()