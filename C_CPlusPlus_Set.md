# 题目
## 题目 1
如果友元函数重载一个运算符时，其参数表中没有任何参数则说明该运算符是：
* 一元运算符
* 二元运算符
* 选项A）和选项B）都可能
* 重载错误

### 正确答案及解析
答案为: **D**

友元函数重载时, 参数列表为 1 , 说明是 1 元, 为 2 说明是 2 元

成员函数重载时, 参数列表为空, 是一元, 参数列表是 1 ,为 2 元

## 题目 2
关于 do 循环体 while(条件表达式)，以下叙述中正确的是？
* 条件表达式的执行次数总是比循环体的执行次数多一次
* 循环体的执行次数总是比条件表达式执行次数多一次
* 条件表达式的执行次数与循环体的执行次数一样
* 条件表达式的执行次数与循环体的执行次数无关

### 正确答案及解析
答案为: **D**

可能一次都没执行条件，可能执行相同的次数(参考 break/continue 等其他跳出循环的语句)

## 题目 3
下面有关 static 类变量和实例变量的描述，正确的有？
* static 类变量又叫静态成员变量，它不需要创建对象就可以已经在内存中存在了
* 在创建实例对象的时候，内存中会为每一个实例对象的每一个非静态成员变量开辟一段内存空间，用来存储这个对象所有的非静态成员变量值
* static 类变量是所有对象共有，其中一个对象将它值改变，其他对象得到的就是改变后的结果
* 实例变量则属对象私有，某一个对象将其值改变，不影响其他对象

### 正确答案及解析
答案为: **ABCD**

A：static 变量在未初始化时存储在 BSS 段，初始化后存储在 data section 数据段，A 正确

B：静态成员则不会开辟空间，B 正确

C：static 变量是类变量，可理解为只有一份，C 正确

D：可理解为：对实例对象，每个实例均有各自的一份变量，改变其值只是改变了自己的那一份，D 正确

## 题目 4
符号 -、\*、$ 分别代表减法、乘法和指数运算，且
a) 三个运算符优先级顺序为：- 最高，\* 其次，$ 最低；
b) 运算符运算时为左结合
则 `5-3*2$2*4-3$2`的结果为  。

### 正确答案及解析
答案为: **256**

```
S1:因为减号的优先级高，先算减法：
    (5 - 3) * 2 $ 2 * (4 - 3) $ 2
    = 2 * 2 $ 2 * 1 $ 2
S2：下一步算乘法：
    (2 * 2) $ (2 * 1）$ 2
    = 4 $ 2 $ 2
S3： 最后求幂
    4 $ 2 $ 2
    = 256
```

## 题目 5
空格处应填写（）。
```C++
#include <iostream>
using namespace std;

class A
{
    public:
        int m;
        int* p;
};

int main()
{
    A s;
    s.m = 10;
    cout<<s.m<<endl; //10
    s.p = &s.m;
    () = 5;
    cout<<s.m<<endl; //5
    return 0;
}
```

### 正确答案及解析
*(s.p) = 5

## 题目 6
下面程序的执行结果：
```C++
class A{
    public:
        long a;
};
class B : public A {
    public:
        long b;
};
void seta(A* data, int idx) {
    data[idx].a = 2;
}
int main(int argc, char *argv[]) {
    B data[4];
    for(int i=0; i<4; ++i){
        data[i].a = 1;
        data[i].b = 1;
        seta(data, i);
    }
    for(int i=0; i<4; ++i){
         std::cout << data[i].a << data[i].b;
    }
    return 0;
}
```

### 正确答案及解析
22221111

这道题应该注意 指针类型加减时步长的问题。

A 大小为 4

B 大小为 8

那么：
void seta(A* data, int idx) {
    data[idx].a = 2;
}

由于传入的实参为 B 类型，大小为 8，而形参为 A 类型，大小为 4

data[idx] 取 data + idx 处的元素，这时指针 data 加 1 的长度不是一个 B 长度，而是一个 A 长度，或者说是 1/2 个 B 长度。

这时该函数中 data[0~3] 指向的是原 data[0].a,data[0].b,data[1].a,data[1].b,

由于隐式类型转换的缘故，data[0].a, data[0].b, data[1].a, data[1].b 处的值全部由于 data[idx].a = 2; 操作变为 2。

这道题如果改为void seta(B* data, int idx)，那么形参中 data 指针加1步长为 8，结果就是 21212121。但是由于步长为 4，所以结果就是 22221111。

## 题目 7
下列代码试图打印数字1-9的全排列组合。
```C++
#include "stdio.h"
#define N 9
int x[N];
int count = 0;

void dump() {
  int i = 0;
  for (i = 0; i < N; i++) {
    printf("%d", x[i]);
  }
  printf("\n");
}

void swap(int a, int b) {
  int t = x[a];
  x[a] = x[b];
  x[b] = t;
}

void run(int n) {
  int i;
  if (N - 1 == n) {
    dump();
    count ++;
    return;
  }
  for (i = ___; i < N; i++) {
    swap(___, i);
    run(n + 1);
    swap(___, i);
  }
}

int main() {
  int i;
  for (i = 0; i < N; i++) {
    x[i] = i + 1;
  }
  run(0);
  printf("* Total: %d\n", count);
}
```
其中 run 函数中缺失的部分应该依次为：

### 正确答案及解析
n, n, n

这是一道分治算法题。这种循环套递归的题目是很难一下子理解的，因此可以把问题的规模减小。

先试 3 个元素，然后我们发现，在循环里面第一句话是那当前的某个数和后面的某个数交换（包括和自己交换，也就是不交换），交换完了之后，后面那个递归就是分治了，也就是从待交换的数的下一个开始直到末尾的一段调用递归用分治搞定。

分治一直调用到最后无法交换的时候，也就是末尾两个指针相遇的时候程序就输出一种排列。所以在递归退出之后，根据程序的逻辑，在当前层循环里面应该只负责当前数和后面的数的交换，而当前数不能变，所以要把现场恢复，因此还需要调用一次 swap 再交换回来就可以了。所以根据程序逻辑，应该选择 C 。自己画一个三个数的排列就可以看明白了， 9 个数太复杂，搞明白关系就可以了。

## 题目 8
下面有关java和c++的描述，错误的是？
* java 是一次编写多处运行，c++ 是一次编写多处编译
* c++ 和 java 支持多重继承
* Java 不支持操作符重载，操作符重载被认为是 c++ 的突出特征
* java 没有函数指针机制，c++ 支持函数指针

### 正确答案及解析
B

JAVA没有指针的概念，被封装起来了，而C++有;

JAVA不支持类的多继承，但支持接口多继承，C++支持类的多继承;

C++支持操作符重载，JAVA不支持;

JAVA的内存管理比C++方便，而且错误处理也比较好;C++的速度比JAVA快。

C++更适用于有运行效率要求的情况，JAVA适用于效率要求不高，但维护性要好的情况。

## 题目 9
下列选项中，会导致用户进程从用户态切换到内核的操作是?
1. 整数除以零
2. sin( )函数调用
3. read系统调用

### 正确答案及解析
仅 I、III

用户态切换到内核态的 3 种方式
* 系统调用
* 异常
* 外围设备的中断

I. 异常

III. 系统调用

## 题目 10
```C++
#include<iostream>
using namespace std;
class MyClass
{
public:
    MyClass(int i = 0)
    {
        cout << i;
    }
    MyClass(const MyClass &x)
    {
        cout << 2;
    }
    MyClass &operator=(const MyClass &x)
    {
        cout << 3;
        return *this;
    }
    ~MyClass()
    {
        cout << 4;
    }
};
int main()
{
    MyClass obj1(1), obj2(2);
    MyClass obj3 = obj1;
    return 0;
}
```
运行时的输出结果是（）

### 正确答案及解析
**122444**

C MyClass obj3 = obj1;

obj3还不存在，所以调用拷贝构造函数输出2，

如果obj3存在，obj3=obj，则调用复制运算符重载函数，输出3

首先程序中存在三个MyClass对象。

前两个对象构造时分别输出1,2

第三个对象是这样构造的MyClass obj3 = obj1;这里会调用拷贝构造函数，输出2

然后三个对象依次析构，输出444

所以最终输出122444

## 题目 11
In C++, what does "explicit" mean? what does "protected" mean?
* explicit-keyword enforces only explicit casts to be valid
* Protected members are accessible in the class that defines them and in classes that inherit from that class.
* Protected members only accessible within the class defining them.
* All the above are wrong

### 正确答案及解析
AB

普通构造函数能够被隐式调用. 而 explicit 构造函数只能被显式调用

## 题目 12
struct 和 class 的区别?
* struct 的成员默认是公有的
* struct 的成员默认是私有的
* 类的成员默认是私有的
* 类的成员默认是公有的

### 正确答案及解析
AC

## 题目 13
下面描述中，正确的是
* 虚函数是没有实现的函数
* 纯虚函数的实现是在派生类中
* 抽象类是没有纯虚函数的类
* 抽象类指针可以指向不同的派生类

### 正确答案及解析
BD

用关键字virtual修饰的成员函数叫做虚函数，虚函数是为了实现多态而存在的，必须有函数体

纯虚函数的声明，是在虚函数声明的结尾加=0，没有函数体。在派生类中没有重新定义虚函数之前是不能调用的

如果一个类中至少含有一个纯虚函数，此时称之为抽象类。所以抽象类一定有纯虚函数

基类类型的指针可以指向任何基类对象或派生类对象