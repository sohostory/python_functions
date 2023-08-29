# Square
my_list = [5, 4, 3]

print(list(map(lambda item: item ** 2, my_list)))


# List Sorting
a = [(0,2), (4,3), (9,9), (10, -1)]

# def second(n):
#     return n[1]
#
# def sort(numbers):
#     return sorted(numbers, key = second)
#
# print(sort(a))

a.sort(key = lambda x: x[1])
print(a)