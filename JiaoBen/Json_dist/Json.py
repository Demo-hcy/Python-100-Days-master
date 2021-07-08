import difflib
import json


def Json_Traverse(indict, pre=None):
    pre = pre[:] if pre else []
    if isinstance(indict, dict):
        for key, value in indict.items():
            if isinstance(value, dict):
                if len(value) == 0:
                    yield pre + [key, '{}']
                else:
                    for d in Json_Traverse(value, pre + [key]):
                        yield d
            elif isinstance(value, list):
                if len(value) == 0:
                    yield pre + [key, '[]']
                else:
                    for v in value:
                        for d in Json_Traverse(v, pre + [key]):
                            yield d
            elif isinstance(value, tuple):
                if len(value) == 0:
                    yield pre + [key, '()']
                else:
                    for v in value:
                        for d in Json_Traverse(v, pre + [key]):
                            yield d
            else:
                yield pre + [key, value]
    else:
        yield indict


def Fill_Open(Json_Traverse):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        JsonValue1 = json.load(f1)
        JsonValue2 = json.load(f2)
    for i in Json_Traverse(JsonValue1):
        print('.'.join(i[0:-1]), ':', i[-1])
    print('----------------------')
    print('|                    |')
    print('|第一个json 已经读取完成 |')
    print('|                    |')
    print('----------------------')
    for j in Json_Traverse(JsonValue2):
        print('.'.join(j[0:-1]), ':', j[-1])
    print('----------------------')
    print('|                    |')
    print('|第二个json 已经读取完成 |')
    print('|                    |')
    print('----------------------')


if __name__ == "__main__":
    file1 = 'C:\\Users\\12569\\Desktop\\a.json'
    file2 = 'C:\\Users\\12569\\Desktop\\b.json'
    Fill_Open(Json_Traverse)
    # Json_Compared()
