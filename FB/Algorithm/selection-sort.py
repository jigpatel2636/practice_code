list1 = [34,5,6,81,0,1,1,5]
#
# for i in range(len(list1)-1):
#     min_value = min(list1[i:])
#     min_index = list1.index(min_value, i)
#     if list1[i] != list1[min_index]:
#         list1[i], list1[min_index] = min_value, list1[i]
# print(list1)


# without using min and index method

for i in range(len(list1)-1):
    min_index = i
    for j in range(i+1, len(list1)):
        if list1[j] < list1[min_index]:
            min_index = j
    if list1[i] != list1[min_index]:
        list1[i], list1[min_index] = list1[min_index], list1[i]
print(list1)