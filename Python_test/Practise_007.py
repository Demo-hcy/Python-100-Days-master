#
# for a in range(1, 100):
#     for b in range(1, 100):
#         if a % b == 0:
#             print("a= ", a, "b= ", b, "可以被整除")
#         else:
#             print("a= ", a, "b= ", b, "不可以被整除")



a  = int(input("请输入范围："))
list1 = []
for b in range(2, a):
    for c in range(2, b):
        if b  % c  == 0:
            break
    else:
        list1.append(b)
print("质数：",list1)

