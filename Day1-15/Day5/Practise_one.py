class Solution:
    def reverse(self, x):
        flag = 1
        if x < 0:
            flag = -1
            x = -x
        R = str(x)[::-1] # 切片操作
        R = int(R)
        if R> 2147483647 or R < -2147483648:
            R = 0
        return R*flag
if __name__ == '__main__':
    S = Solution()
    ret = S.reverse(123456789)
    print(ret)