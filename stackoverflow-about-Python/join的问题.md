## join的问题

为什么是 `string.join(list)` 而不是 `list.join(string)`?

比如：

```python
my_list = ["Hello", "world"]
print(my_list.join("-"))
# Produce: "Hello-world"
```

其实因为所有的可迭代对象都能被 `join`，不仅仅是列表，但一般情况下我们要 `join` 的都是字符串

比如：

```python
import urllib2
print '\n############\n'.join(urllib2.urlopen('http://data.stackexchange.com/users/7095'))
```

