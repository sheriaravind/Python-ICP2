import operator

list = ['Kansas','Chicago','California','Milwaukee']
data = {}
for item in list:
    length = len(item)
    data[item] = length
Sorted_Data = sorted(data.items(), key=operator.itemgetter(1))
print(Sorted_Data[-1])