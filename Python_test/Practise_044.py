adist ={'a':1,'b':2}
print(adist.get('a'))
print(adist.get('d',3))
print(adist.items())
print(adist.keys(),adist.values())
print(adist.update({'b':4}),adist.update({'c':5}),adist)
print(adist.setdefault('d',0),adist.setdefault('a'),adist)
print(adist.pop('d'),adist)
print(adist.popitem(),adist)