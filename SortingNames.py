
def sorting_names_by_length_descending():
    list_names = input().split(', ')
    sorted_names = sorted(list_names, key=lambda x: (-len(x), x))
    print(sorted_names)


sorting_names_by_length_descending()



