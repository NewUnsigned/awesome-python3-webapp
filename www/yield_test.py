import types


# def fab(max):
#     n, a, b = 0, 0, 1
#     L = []
#     while n < max:
#         L.append(b)
#         a, b = b, a + b
#         n = n + 1
#     return L

class Fab(object):
    
    def __init__(self, max):
        self.max = max
        self.n, self.a, self.b = 0, 0, 1

    def __iter__(self):
        return self

    # python3中迭代器需要实现__next__方法，之前版本是next方法
    def __next__(self):
        if self.n < self.max:
            r = self.b
            self.a, self.b, = self.b, self.a + self.b
            self.n = self.n + 1
            return r
        raise StopIteration()



# 一个带有yield的函数，就是一个generator，它和普通的函数不同，生成一个generator看起来像函数
# 调用，但不会执行函数代码，知道对其调用__next__()（在for循环中会自动调用__next__()）才开始
# 执行。虽然执行流程扔按照函数的执行流程，但每执行到一个yield语句就会中断，并返回一个迭代值，下
# 次执行时从yield的下一个语句继续执行。

def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1

# fab = fab(5)
# print(isinstance(fab, types.GeneratorType))
# for n in fab:
#     print(n)

astr = 'ABC'
alist = [1, 2, 3]
adict = {'name':'wangbm','age':18}
agen = (i for i in range(4, 8))

def gen(*args, **kw):
    for item in args:
        yield from item


new_list = gen(astr, alist, adict, agen)
print(list(new_list))
