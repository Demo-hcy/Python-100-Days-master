def Conversion():


    if Danwei == 'YL' or Danwei== '英里':
        print(f'%f英里 = %f公里'%(Long,Long/0.6214))

    elif Danwei == 'GL' or Danwei== '公里':
        print(f'%f公里 = %f英里'%(Long,Long*0.6214))
    else:
        print("请输入正确的单位")

if __name__ == '__main__':
    Long = float(input("请输入长度："))
    Danwei = input('请输入单位: ')
    Conversion()