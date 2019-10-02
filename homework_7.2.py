def remove_shorts(strings_list):
    string = [element for element in strings_list if len(element) > 4]
    print(string)


# remove_shorts(['telegram', 'sport', 'call', 'football', 'jet'])
remove_shorts(['zombie', 'vision', 'cat', 'ring', 'telescope'])
