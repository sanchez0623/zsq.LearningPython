# dict——字典——{key：value}——无序
# key-value类型
# key必须是不可变的类型

# 不支持 下标、切片

print(type({
    1: 1,
    2: 2,
    3: 3
}))
print(type({
    '1': 1,
    1: 1,
    2: 2,
    3: 3
}))

print({
    1: 1,
    2: 2,
    3: 3
})
print({
    '1': 1,
    1: 1,
    2: 2,
    3: 3
})

#异常：TypeError: unhashable type: 'list'
print({
    [1, 2]: 1,
    2: 2,
    3: 3
})

#使用tuple作为key，正常
print({
    (1, 2): 1,
    2: 2,
    3: 3
})

# 如何定义空字典？
print(type({}))
