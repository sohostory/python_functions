some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []
# for value in some_list:
#     if some_list.count(value) > 1:
#         if value not in duplicates:
#             duplicates.append(value)

duplicates = list(set(letter for letter in some_list if some_list.count(letter) > 1))

print(duplicates)