

def sort_list_custom():
    list_to_do = []
    while True:
        note = input()

        if note == 'End':
            break
        list_to_do.append(note)
    sorted_list_to_do = sorted(list_to_do, key=lambda x: int(x.split('-')[0]))
    result = [note.split('-')[1] for note in sorted_list_to_do]
    return result


print(sort_list_custom())






