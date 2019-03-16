
print('1'+'2');

print('hello' * 3);

print('hello world'[0]);
print('hello world'[3]);
print('hello world'[4]);
print('hello world'[-1]);
print('hello world'[-3]);


#步长
#[x:y] x为闭区间，y为开区间
print('hello world'[0:4]);
print('hello world'[0:5]);
print('hello world'[0:-1]);


#输出world
print('hello world'[6:10]);#输出worl
print('hello world'[6:11]);#输出world
print('hello world'[6:20]);#输出world

print('hello world'[6:-1]);#输出worl
print('hello world'[6:0]);#输出‘’
print('hello world'[6:-0]);#输出‘’

#适合很长的字符串
print('hello world'[6:]);#输出world


print('hello python java c# js php ruby'[6:]);
print('hello python java c# js php ruby'[:-4]);
print('hello python java c# js php ruby'[-4:]);



#切片
# print([1,2,3,4,5,6][0:]);
# print([1,2,3,4,5,6][:-1]);
# print([1,2,3,4,5,6][0:8:2]);
