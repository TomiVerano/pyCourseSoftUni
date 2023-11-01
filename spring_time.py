def start_spring(**kwargs):
    dict_new = {}
    result = ""
    for key, value in kwargs.items():
        if value not in dict_new:
            dict_new[value] = []
            dict_new[value].append(key)
    sorted_collections = sorted(dict_new.items(),key=lambda x: (-len(x[1]), x[0]))
    for tuple in sorted_collections:
        t_object = tuple[0]
        list_object = tuple[1]
        sorted_collections = sorted(list_object)
        result += f"{t_object}:\n"
        for obj in sorted_collections:
            result += f"-{obj}\n"
    return result.strip()


example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",}


print(start_spring(**example_objects))