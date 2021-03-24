import os
import timeit
import multiprocessing
import hashlib


def getHash(f):
    # line=f.readline()
    md5_hash = hashlib.md5()
    while True:
        # md5_hash.update(line)                                、
        # line=f.readline()
        content = f.read(1024)
        if not content:
            break
        md5_hash.update(content)
    return md5_hash.hexdigest()


def readFilename(path, allfile):
    filelist = os.listdir(path)

    for filename in filelist:
        filepath = os.path.join(path, filename)
        # filepath=unicode(filepath,"utf-8")

        if os.path.isdir(filepath):
            readFilename(filepath, allfile)
        else:
            allfile.append(filepath)

    return allfile


def begin():
    ff1 = "C:\Users\zgd\Desktop\zgddgz"
    ff2 = "C:\Users\zgd\Desktop\gdzhang"
    allJPG1 = []
    allJPG1 = readFilename(ff1, allJPG1)
    # print allJPG1

    allJPG2 = []
    allJPG2 = readFilename(ff2, allJPG2)
    # print allJPG2

    count = 0
    for a1 in allJPG1:
        for b1 in allJPG2:
            # print a1,b1
            with open(a1, 'r') as f1, open(b1, 'r') as f2:
                m1 = getHash(f1)
                # print m1
                m2 = getHash(f2)
                # print m2

            if m1 == m2:
                count = count + 1
                print
                count
                print
                "%s = %s" % (a1, b1)

                filepath = 'C:\Users\zgd\Desktop\zhangniu\Link.txt'
                # filepath = 'H:\\RINS1000\\' + 'Link.txt'
                with open(filepath, 'a') as fp:
                    fp.write(a1 + "\t\t")
                    fp.write(b1.split("\\")[-1] + "\n")

                fp.close()
            f1.close()
            f2.close()


if __name__ == '__main__':
    start = timeit.default_timer()

    pool = multiprocessing.Pool(32)
    pool.apply(func=begin)
    pool.close()
    pool.join()

    end = timeit.default_timer()
    print
    str(end - start)


def genSizeFile(fileName, fileSize):
    #file path
    filePath="Data"+fileName+".txt"

    # 生成固定大小的文件
    # date size
    ds=0
    with open(filePath, "w", encoding="utf8") as f:
        while ds<fileSize:
            f.write(str(round(random.uniform(-1000, 1000),2)))
            f.write("\n")
            ds=os.path.getsize(filePath)
    # print(os.path.getsize(filePath))

# start here.
genSizeFile("1k",1*1024)
