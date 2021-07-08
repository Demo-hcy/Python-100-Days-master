import json as js
import difflib


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


def Json_Compared(Json_Traverse):
    f = open('C:\\Users\\12569\\Desktop\\test1.json', encoding='UTF-8')
    m = open('C:\\Users\\12569\\Desktop\\test2.json', encoding='UTF-8')

    x = js.load(f)
    y = js.load(m)
    # for my_key in x.keys():
    #     value_eval = x[str(my_key)]
    #     value_test = y[str(my_key)]
    #     diff = difflib.SequenceMatcher(None, value_eval, value_test).quick_ratio()
    #     print(my_key, diff)
    for my_key in Json_Traverse.key():
        value_eval = x[str(my_key)]
        value_test = y[str(my_key)]
        diff = difflib.SequenceMatcher(None, value_eval, value_test).quick_ratio()
        print(my_key, diff)


if __name__ == '__main__':
    Json_Compared()
