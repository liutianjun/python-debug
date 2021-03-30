import sys

s = '\xd6\xc2\xc3\xfc\xb4\xed\xce\xf3: \xca\xfd\xbe\xe2 \"bbs-go\" \xb2\xbb\xb4\xe6\xd4\xda (SQLSTATE 3D000)'


def decodeStr():
    ss = s.encode('raw_unicode_escape').decode('gbk')
    print(str(sys._getframe().f_lineno) + "行: " + ss)


if __name__ == '__main__':
    decodeStr()
