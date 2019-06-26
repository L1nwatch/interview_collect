//题目描述
//你是火星上S公司CEO，对公司研发产品进行估值营销，假设公司有N款产品（1=<N<=100），每款产品的销售额为整数pi，（0<pi<=100亿），
//
//此时，如果产品进入了Gartner魔力象限，则估值为 pi*t（2=<t<=10，t为整数）,否则估值为pi*2。
//
//现在期望你计算并输出S公司不同产品的估值之和，每个值一行。 （有多组数据，见输入输出示例）
//
//输入
//输入规格为，有多组数据，每组数据第一行一个整数N，表示N款产品
//
//第2行至第N+1行为
//
//p1 s1
//
//p2 s2
//
//...
//
//pi si（i=N,si=0表示未进入魔力象限，si=1表示进入了魔力象限。 pi，si空格隔开）；
//
//第N+2行为t。 N=0表示结束，不处理。
//
//输出
//输出公司估值总和，每组数据对应一行，一个值。
//3
//8 0
//9 0
//10 1
//2
//3
//8 0
//9 0
//10 1
//8
//2
//7 1
//7 0
//3
//0



//#include <cstdio>
//#include <cstring>
//#include <string>
//#include <map>
//#include <vector>
//#include <algorithm>
//#include <queue>
//#include <stack>
//#include <cmath>

#include <iostream>
using namespace std;

int main()
{
	int n;
	int t;
	while(cin>>n && n)
	{
		long long sum = 0,temp = 0;
		long long p,s;  
		for(int i = 0;i<n;++i)
		{
			cin>>p>>s;
			if(s) temp += p;
			else sum += p * 2;
		}
		cin>>t;
		sum = sum + temp * t;
		cout<<sum<<endl;
	}
	return 0;
}









