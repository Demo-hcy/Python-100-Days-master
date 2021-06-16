mystr="Beautiful is better than ugly"
print("swapcase demo:\t",mystr.swapcase())  #swapcase 小写转换为大写，大写转换为小写
print("upper demo:\t",mystr.upper()) # upper 将字符串小写全部转换为大写
print("lower demo:\t",mystr.lower()) # lower 将字符串大写全部转换为小写
print("title demo:\t",mystr.title()) # title 将字符串中单词第一个字符全部改为大写
print("istitle demo:\t",mystr.istitle()) # istitle 检测字符串中的单词是否为首字母大写
print("islower demo:\t",mystr.islower()) # islower 检测字符串中的单词是否为均小写字母
print("capitalize demo:\t",mystr.capitalize()) # capitalize 将字符串第一个字母大写
print("find demo:\t",mystr.find("u") ) # find 获得字符串中某一字符的起始位置，无法返回 -1【print("find demo:\t",mystr.find("p") ) 】
print("count demo:\t",mystr.count("y")) # count 获得字符串某一字符的数目
print("split demo:\t",mystr.split()) # split 分割字符串
print("join demo:\t"," ".join("1,a,b,c,f")) # join 连接字符串
print("len demo:\t",len(mystr)) # len 获取字符串长度
