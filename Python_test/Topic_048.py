# import json
#
#
# def cmp(src_data, dst_data):
#     if isinstance(src_data, dict):
#         """若为dict格式"""
#         for key in dst_data:
#             if key not in src_data:
#                 print("src不存在这个key")
#         for key in src_data:
#             if key in dst_data:
#                 """递归"""
#                 cmp(src_data[key], dst_data[key])
#             else:
#                 print("dst不存在这个key")
#     elif isinstance(src_data, list):
#         """若为list格式"""
#         if len(src_data) != len(dst_data):
#             print("list len: '{}' != '{}'".format(len(src_data), len(dst_data)))
#         for src_list, dst_list in zip(sorted(src_data), sorted(dst_data)):
#             """递归"""
#             cmp(src_list, dst_list)
#     else:
#         if str(src_data) != str(dst_data):
#             print(src_data)
#
# def Fill_Open(cmp):
#     with open(file1, 'r') as f1, open(file2, 'r') as f2:
#         JsonValue1 = json.load(f1)
#         JsonValue2 = json.load(f2)
#     cmp(JsonValue1, JsonValue2)
# if __name__ == "__main__":
#     file1 = 'C:\\Users\\12569\\Desktop\\test1.json'
#     file2 = 'C:\\Users\\12569\\Desktop\\test2.json'
#     Fill_Open(cmp)

# def cmp(src_data, dst_data):
#     if isinstance(src_data, dict):
#         """若为dict格式"""
#         for key in dst_data:
#             if key not in src_data:
#                 print("src不存在这个key")
#         for key in src_data:
#             if key in dst_data:
#                 """递归"""
#                 cmp(src_data[key], dst_data[key])
#             else:
#                 print("dst不存在这个key")
#     elif isinstance(src_data, list):
#         """若为list格式"""
#         if len(src_data) != len(dst_data):
#             print("list len: '{}' != '{}'".format(len(src_data), len(dst_data)))
#         for src_list, dst_list in zip(sorted(src_data), sorted(dst_data)):
#             """递归"""
#             cmp(src_list, dst_list)
#
#     elif isinstance(src_data, tuple):
#         if len(src_data) == len(dst_data):
#             print("tuple len: '{}' != '{}'".format(len(src_data), len(dst_data)))
#             for src_list, dst_list in zip(sorted(src_data), sorted(dst_data)):
#                 """递归"""
#                 cmp(src_list, dst_list)
#     else:
#         if str(src_data) != str(dst_data):
#             print(src_data)
#
# dict1 = {"networkInfo":{"networkType":"wired","wirelessSupport":"none","ip":"192.168.52.10","gateway":"192.168.52.1","mask":"255.255.255.0","apnInfo":{"apn":"","password":"","auth":""},"mac":"00:50:c2:45:26:ce"}}
# dict2 = {"networkInfo":{"networkType":"wired","wirelessSupport":"none","ip":"192.168.52.10","gateway":"192.168.52.1","mask":"255.255.255.0","apnInfo":{"apn":"","user":"","password":"","auth":""},"mac":"00:50:c2:45:26:ce"}}
# cmp(dict1, dict2)


# 比对数据
def compare_data(set_key, src_data, dst_data, noise_data, num):
    if isinstance(src_data, dict) and isinstance(dst_data, dict):
        """若为dict格式"""
        for key in dst_data:
            if key not in src_data:
                print("src不存在这个key")
                noise_data[key] = "src不存在这个key"
        for key in src_data:
            if key in dst_data:
                if src_data[key] != dst_data[key] and num == 1:
                    noise_data[key] = "容忍不等"
                if src_data[key] != dst_data[key] and num == 2:
                    noise_data[key] = {}
                    noise_data[key]["primary"] = src_data[key]
                    noise_data[key]["candidate"] = dst_data[key]
                """递归"""
                compare_data(key, src_data[key], dst_data[key], noise_data, num)
            else:
                noise_data[key] = ["dst不存在这个key"]
    elif isinstance(src_data, list) and isinstance(dst_data, list):
        """若为list格式"""
        if len(src_data) != len(dst_data) and len(set_key) != 0:
            print("list len: '{}' != '{}'".format(len(src_data), len(dst_data)))
            noise_data[set_key]["primary"] = str(src_data)
            noise_data[set_key]["candidate"] = str(dst_data)
            return
        if len(src_data) == len(dst_data) and len(src_data) > 1:
            for index in range(len(src_data)):
                for src_list, dst_list in zip(sorted(src_data[index]), sorted(dst_data[index])):
                    """递归"""
                    compare_data("", src_list, dst_list, noise_data, num)
        else:
            for src_list, dst_list in zip(sorted(src_data), sorted(dst_data)):
                """递归"""
                compare_data("", src_list, dst_list, noise_data, num)
    else:
        if str(src_data) != str(dst_data):
            print("src_data", src_data, "dst_data", dst_data)
    return noise_data

dict1 = {"networkInfo":{"networkType":"wired","wirelessSupport":"none","ip":"192.168.52.10","gateway":"192.168.52.1","mask":"255.255.255.0","apnInfo":{"apn":"","password":"","auth":""},"mac":"00:50:c2:45:26:ce"}}
dict2 = {"networkInfo":{"networkType":"wired","wirelessSupport":"none","ip":"192.168.52.10","gateway":"192.168.52.1","mask":"255.255.255.0","apnInfo":{"apn":"","user":"","password":"","auth":""},"mac":"00:50:c2:45:26:ce"}}
compare_data(0,dict1, dict2,0,0)