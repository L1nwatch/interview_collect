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

int char_to_int(char a)
{
	int result = int(a - '0');
	return result;
}

int main()
{
	int n;
	cin>>n;
	char a,b,c,d,p;
	cin>>a>>b>>p>>c>>d;
	
	int x = char_to_int(a)*10 + char_to_int(b);
	int y = char_to_int(c)*10 + char_to_int(d);
	
	if(n == 24)
	{
		if(x<=23 && y<=59)
				{
					cout<<a<<b<<p<<c<<d<<endl;
				}
		if(x>23 && y<=59)
				{
					cout<<0<<b<<p<<c<<d<<endl;
				}
		if(x<=23 && y >59)
				{
					cout<<a<<b<<p<<0<<d<<endl;
				}
		if(x>23&&y>59)
				cout<<0<<b<<p<<0<<d<<endl;
	}
	else
	{
//		if(x == 12)
//		{
//			if(y == 0)
//				cout<<a<<b<<p<<c<<d<<endl;
//			if(y>0 &&y<=59)
//				cout<<0<<b<<p<<c<<d<<endl;
//			if(y>59)
//				cout<<0<<b<<p<<0<<d<<endl;
//		}
		if(!x)
		{
			if(y <=59)
				cout<<1<<b<<p<<c<<d<<endl;
			if(y>59)
				cout<<1<<b<<p<<0<<d<<endl;
		}
		if(x<=12 && x>0 && y<=59)
				{
					cout<<a<<b<<p<<c<<d<<endl;
				}
		if(x>12 && y<=59)
				{
//					cout<<0<<b<<p<<c<<d<<endl;
					if( b == '0')
						cout<<1<<b<<p<<c<<d<<endl;
					else
						cout<<0<<b<<p<<c<<d<<endl;
				}
		if(x<=12 && x>0 && y >59)
				{
					cout<<a<<b<<p<<0<<d<<endl;
				}
		if(x>12&&y>59)
				{
					if(b == '0')
						cout<<1<<b<<p<<0<<d<<endl;
					else
						cout<<0<<b<<p<<0<<d<<endl;
				}
	}
	return 0;
}
