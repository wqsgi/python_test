__author__ = 'weiqisong'


class MetaClass(type):
    def __init__(self, name, base, attrs):
        print("name is %s" % name)
        print("base is %s" % base)
        for key, value in attrs.items():
            print("key=%s,value=%s" % (key, value))


class B(object, metaclass=MetaClass):
    def __call__(self, *args, **kwargs):
        return args[0]


b = B()
print(b(1211))
