"""myswq = '''
[a:1,b:2,c:3]
[a:3,b:3,c:8]
[a:7,c:2:m:7,r:4]
[a:2,c:2:m:7,r:4]
[a:2,b:2,c:7,o:5]
'''
return [a:1,b:2,c:3],[a:7,c:2:m:7,r:4],[a:2,b:2,c:7,o:5]
"""

myseq = '''[a:1,b:2,c:3]
[a:3,b:3,c:8]
[a:7,c:2:m:7,r:4]
[a:2,c:4:m:6,r:4]
[a:3,b:2,c:7,o:5]'''


def eve(i):
    evest = ''
    for x in [y for y in range(len(i)) if y % 2 == 0]:
        evest += i[x]
    return evest

myseq = myseq.split('\n')
lt = []
for i in myseq:
    lt.append(eve(i.replace('[','').replace(']','').replace(':','').replace(',','')))
l1,l2=[],[]
for i in range(len(lt)):
    if not lt[i] in l2:
        l2.append(lt[i])
        l1.append(myseq[i])
print(l1)

if __name__ == '__main__':
    eve([])
