#coding:utf-8

seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print(list(enumerate(seasons)))

# 小标从1开始
print(list(enumerate(seasons, start=1)))

#################
# 普通的for循环和使用enumerate的for循环
#################
# 普通的for循环
i = 0
seq = ['one', 'two', 'three']
for element in seq:
    print(i, seq[i])
    i += 1

print('\n#################\n')
# for循环使用enumerate
seq = ['one', 'two', 'three']
for i, element in enumerate(seq):
    print(i, element)