def detect_palindromes(strings):
    values = (True for value in strings if value == value[::-1])
    dict = {key: value for key, value in zip(strings, values)}
    print(dict)

#
detect_palindromes(['madam', 'joy', 'fish'])

# f = ['madam', 'joy', 'fish']
# f1 = []
# for element in f:
#     if element == element[::-1]:
#         f1.append(True)
#     else:
#         f1.append(False)
#
# print zip(f: f1)
