"""
sys	跟Python解释器相关的变量和函数
sys.argv    传递到Python脚本的命令行参数列表，第一个元素是程序本身路径
sys.executable  返回Python解释器在当前系统中的绝对路径
sys.exit([arg]) 程序中间的退出，arg=0为正常退出
sys.path    返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
sys.platform    返回操作系统平台名称，Linux是linux2，Windows是win32
sys.stdout.write(str)   输出的时候把换行符\n去掉
val = sys.stdin.readline()[:-1] 拿到的值去掉\n换行符
sys.version 获取Python解释程序的版本信息


os	和操作系统相关的功能，例如：os.listdir()、os.remove()
re	和正则表达式相关的功能，例如：re.compile()、re.search()
math	和数学运算相关的功能，例如：math.pi、math.e、math.cos
logging	和日志系统相关的类和函数，例如：logging.Logger、logging.Handler
json / pickle	实现对象序列化和反序列的模块，例如：json.loads、json.dumps
hashlib	封装了多种哈希摘要算法的模块，例如：hashlib.md5、hashlib.sha1
urllib	包含了和URL相关的子模块，例如：urllib.request、urllib.parse
itertools	提供各种迭代器的模块，例如：itertools.cycle、itertools.product
functools	函数相关工具模块，例如：functools.partial、functools.lru_cache
collections / heapq	封装了常用数据结构和算法的模块，例如：collections.deque
threading / multiprocessing	多线程/多进程相关类和函数的模块，例如：threading.Thread
concurrent.futures / asyncio	并发编程/异步编程相关的类和函数的模块，例如：ThreadPoolExecutor
base64	提供BASE-64编码相关函数的模块，例如：bas64.encode
csv	和读写CSV文件相关的模块，例如：csv.reader、csv.writer
profile / cProfile / pstats	和代码性能剖析相关的模块，例如：cProfile.run、pstats.Stats
unittest	和单元测试相关的模块，例如：unittest.TestCase

"""


# import sys
# sys.path="D:\公司\二代项目\动环盒子"
# print("-----------------")
# print(sys.argv[0])
#
# print("-----------------")
# print(sys.platform)
#
# print("-----------------")
# print(sys.path)
#
# print("-----------------")
# print("hello word!")
# sys.exit()
# print("your is pythoner")



