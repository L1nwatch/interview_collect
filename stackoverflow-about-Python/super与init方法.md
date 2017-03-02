## super与init方法

`super()` 的好处是可以避免直接使用父类的名字，主要用于多重继承。

注意在 Python3 里面语法有所改变，可以用 `super().__init___()` 代替 `super(ChildB, self).__init__()`

DEMO：

```python
class Base(object):
    def __init__(self):
        print "Base created"

class ChildA(Base):
    def __init__(self):
        Base.__init__(self)

class ChildB(Base):
    def __init__(self):
        super(ChildB, self).__init__()

class ChildC(Base):
    def __init__(self):
        super().__init__()
        
print ChildA(), ChildB(), ChildC()
```

