def change_case(string):
    string1 = ((element.upper(), element.lower()) for element in string if
               element.islower() elif element.isupper())
    # string2 = [element.lower() for element in string if element.isupper()]
    print(string1)


change_case("Hi! I'm Jim :)")

# change = "Hi! I'm Jim :)"

# for element in change:
#     if element.islower():
#         print(element.upper())
#
#     elif element.isupper():
#         print(element.lower())
