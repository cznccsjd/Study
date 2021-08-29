#coding:utf-8
"""
给定数组，前后元素位置对调
"""
my_list = [1,2,3,4,5]
my_list2 = [9,8,7,6]

m = len(my_list)
n = len(my_list2)

for i in range(int(m/2)):
    tmp_i = my_list[i]
    my_list[i] = my_list[m-1-i]
    my_list[m-1-i] = tmp_i

for j in range(int(n/2)):
    tmp_j = my_list2[j]
    my_list2[j] = my_list2[n-1-i]
    my_list2[n-1-i] = tmp_j

print(f'my_list前后元素互换位置后的新列表为{my_list}')
print(f'my_list2前后元素互换位置后的新列表为{my_list2}')