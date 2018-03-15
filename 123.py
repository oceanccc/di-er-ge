#定义一个函数
def name():
    print('hello')
name()
print(type(name))
#调取函数
def student(name):    
    print("Welcome", name)
a='X'
student(a)
#必须参数
def use(name,age):
    print('你的名字是：',name,'你的年龄是：',age)
name='XX'
age='12'
use(name,age)
#关键字参数
def use(name,age):
    print('你的名字是：',name,'你的年龄是：',age)
use(name='xx',age='13')
#默认参数
def use(name='X',age='15'):
    print('你的名字是：',name,'你的年龄是：',age)
use()
def use(name='X',age='15'):
    print('你的名字是：',name,'你的年龄是：',age)
use('asd')
#不定长参数  元组形式 
def aa(*abc):
    for i in range(len(abc)):
        if i%2==0:
            print(abc[i])
aa(1,2,3,4,5,6)
        
#不定长参数  列表形式        
def aa(*abc):
    for i in range(len(abc)):
        if i%2==0:
            print(abc[i])
aa(*[1,2,3,4,5,6])

#不定长参数  字典形式1
def aa(**abc):
            print(abc['bb'])
aa(bb='a',name='x',cc='g')

#不定长参数  字典形式2
def aa(**abc):
            print(abc['name'])
aa(**{'name':'Y'})

#不定长参数  字典形式2
def aa(**abc):
            print(abc['name'])
a={'name':1}
aa(**a)

#匿名函数
f=lambda x,y,z:x+y*z
a=f('W','M',4)
print(a)
#标砖函数的返回
def aa(x,y,z):
    return x+y*z
aa('xx','yy',4)
print(aa)
r=aa('xx','yy',4)
print(r[:5])

#递归函数实现阶乘的执行演示
#本函数受限于阶乘的概念要求n是一个大于0的正整数
def f(n):
    print(n)
    if n==1:
        return 1
    return f(n-1) * n
a=f(20)
print(a)




















