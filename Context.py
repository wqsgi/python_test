from contextlib import contextmanager

__author__ = 'weiqisong'


@contextmanager
def make_content():
    print("enter")
    try:
        print("start")
        yield "abc"
    except RuntimeError:
        print("error")
    finally:
        print("end")


with make_content() as value:
    print(value)
    print("close")

print("-----")

