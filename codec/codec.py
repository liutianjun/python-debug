import sys
import time

s = '\xd6\xc2\xc3\xfc\xb4\xed\xce\xf3: \xca\xfd\xbe\xe2 \"bbs-go\" \xb2\xbb\xb4\xe6\xd4\xda (SQLSTATE 3D000)'


def decodeStr():
    ss = s.encode('raw_unicode_escape').decode('gbk')
    print(time.strftime('%Y/%m/%d %H:%M:%S ', time.localtime(time.time())) + __file__ + ":" + str(
        sys._getframe().f_lineno) + " 函数名:" + str(sys._getframe().f_code.co_name) + "(): " + ss)


if __name__ == '__main__':
    decodeStr()
