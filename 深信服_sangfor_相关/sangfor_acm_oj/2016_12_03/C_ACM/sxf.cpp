//题目描述
//火星探险队到了一个洞穴，里面有一座桥，由石板铺就，石板上面有大写英文字母，经探索发现，只有
//
//标有元音字母A，E，I，O，U，Y的字母的石板是安全的，其它石板都会翻动。
//
//只有从桥左边位置走到桥右边位置才能算脱险。对于不是连续元音的石板，只能采用跳过去的方法。
//
//如下石板桥
//
//
//
//如果跳跃能力达不到4个格是无法穿越石板桥的。
//
//帮忙算一下探险队要安全脱险的最小跳跃能力是多少。
//
//输入
//一个字符串只有大写英文字母。
//
//长度最大为100
//
//输出
//一个整数，代表最小的跳跃能力。
//样例输入
//ABABBBACFEYUKOTT
//AAA
//样例输出
//4
//1
#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <map>
#include <vector>
#include <algorithm>
#include <queue>
#include <stack>
#include <cmath>
 
using namespace std;

int main()
{
	string s;
	int len;
	while(cin>>s)
	{
		int r = 1,min = 1;
		len = s.length();
		for(int i = 0;i<len;++i)
		{
			if(s[i] == 'A' || s[i] == 'E' || s[i] == 'I' || s[i] == 'O' || s[i] == 'U' || s[i] == 'Y')
			{
				if(r>min) 
				{
					min = r;
					r = 1;
				 } 
				else
					r = 1;			
			}
			else
			{
				++r;
				if(r>min)	min = r;
//				cout<<s[i]<<" "<<r<<endl; 
			}
		}
		cout<<min<<endl;
	}
 	return 0;
} 

















