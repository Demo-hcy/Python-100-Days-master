# message= 'hello the world'
# print(message.replace("o","l"))
#
# import re
#
# message = 'hello, world!'
# pattern = re.compile('[l]')
# print(pattern.sub('#', message))

filenames = ['a12.txt', 'a8.txt', 'b10.txt', 'b2.txt', 'b19.txt', 'a3.txt']
dict = {'a8.txt':'a08.txt','b2.txt':'b02.txt','a3.txt':'a03.txt'}
genhuan_filenames = [dict[x] if x in dict else x for x in filenames]
new_filenames = sorted(genhuan_filenames)
dict = {'a08.txt':'a8.txt','b02.txt':'b2.txt','a03.txt':'a3.txt'}
Tihuan_filenames = [dict[x] if x in dict else x for x in new_filenames]
print(Tihuan_filenames)

# filenames = ['a12.txt', 'a8.txt', 'b10.txt', 'b2.txt', 'b19.txt', 'a3.txt']
# new_filenames = sorted(filenames)
# print(new_filenames)