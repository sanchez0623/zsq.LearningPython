#list

print([1,2,3,4,5]);
print(type([1,2,3,4,5]));

print([1,2,"hello","world",True,[1,2],[True,False]]);
print(type([1,2,"hello","world",True,[1,2],[True,False]]));

#基础操作

#返回单个元素
print(["1","2","3","4"][0]);

#返回list
print(["1","2","3","4"][0:2]);
print(["1","2","3","4"][-1:]);


print(["1","2","3","4"]+[5,6]);
print(["1","2","3","4"]*3);


# 序列共有操作
# in | not in
print(3 in [1,2,3,4,5,6]);
print(10 in [1,2,3,4,5,6]);
print(3 not in [1,2,3,4,5,6]);

# len() 长度
# max() 最大值
# min() 最小值


# 编码
# ascii编码
print(ord('e'));
print(ord('w'));
print(ord(' '));