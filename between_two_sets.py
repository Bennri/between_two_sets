#!/bin/python

# n, m = 2, 3
# a = [2, 4, 8]
# b = [16, 32, 96]

# n, m = 4, 5
# a = [1, 3]
# b = [18, 27, 54]

# a = [1]
# b = [100]

# sample data
a = set([2 ,3, 6])
b = set([42, 84])

# get all multiplies, element of a * i until the lowest value of b
k = [[elem * i for i in range(1, min(b) + 1) if elem * i <= min(b)] for elem in a]
# [[a[0] * i_1, ..., a[0] * i_n], [a[1] * i_1, ..., a[1] * i_n], ...]

# because a factor must be one of all elements in a, just use the equal values
k = sorted(list(set.intersection(*map(set, k))))

# get to know which number from k is a factor of element in b
# a zero indicates a factor, every other value means remainder
# result is a list which contains len(b) lists,
indicate = [[elem % j for j in k] for elem in b]

# get possible matches, the list will contain True for the indices which
# are possible values
# indication by boolean values (not necessary)
indicator_boolean = map(lambda x: map(lambda y: y == 0, x), indicate)

# zip the boolean with the actual value
bool_and_val = map(lambda x: zip(x, k), indicator_boolean)
# get indices of values which are not between both
indices_not_between = [[k.index(elem[1]) for elem in x if elem[0] is False] for x in bool_and_val]

# flatting the list
flatten = lambda l: [i for sub_list in l for i in sub_list]

# remove duplicates
indices_not_between_set = set(flatten(indices_not_between))

# creation of list containing numbers between a and b
values_between = [k[i] for i in range(len(k)) if not i in indices_not_between_set]

print len(values_between)
print values_between
