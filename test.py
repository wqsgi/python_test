import struct

__author__ = 'weiqisong'

list = [i + 5 for i in range(30) if i % 2 == 0]
list[1]=[1,2,3]
for v in list:
    print(v)





sum = lambda x,y:x+y
print(sum(1,2))


expr="sd"
print("c_%s" % expr)

