## 在Windows下安装pip

### Python3.4+

Python3.4 已经自带 pip 了，自带的包管理器中加入了 Ruby、Nodejs、Haskell、Perl、Go 等其他几乎所有的开源社区流行语言

### Python2.x 和 Python <=3.3

*   官方指南，下载 `get-pip.py`，然后运行
*   另一种方法：Python 包的安装器：`.msi`，可以在这个[网站](http://www.lfd.uci.edu/~gohlke/pythonlibs/)上下载

### 代理问题

可能需要 HTTP 代理，把环境变量设置为 `http_proxy` 和 `https_proxy`

```python
http://proxy_url:port
http://username:password@proxy_url:port
```

如果用的是微软的 NTLM 代码，还是换一个友好一点的吧

### 找不到 `vcvarsall.bat`

Pythoon 中有的模块是用 C/C++ 编写的，pip 将尝试从源码进行编译。如果没有安装或设置过 C/C++ 编译器，将会看到这个错误

```shell
Error: Unable to find vcvarsall.bat
```

可以通过安装像 MinGw 或者 VC++ 这样的编译器来解决。微软实际上已经子弟啊了一个为 Python 准备的编译器：`vcpython27`