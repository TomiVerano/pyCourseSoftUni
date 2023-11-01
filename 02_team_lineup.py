def team_lineup(*args):
    result = ""
    sorting_data = {}
    for entry in args:
        p_name = entry[0]
        print(p_name)
        p_country = entry[1]
        print(p_country)
        if p_country not in sorting_data:
            sorting_data[p_country] = []
        sorting_data[p_country].append(p_name)

    sorted_collections = sorted(sorting_data.items(), key=lambda x: (-len(x[1]), x[0]))

    for key, value in sorted_collections:
        result += f"{key}:\n"
        for player in value:
            result += f"  -{player}\n"
    return result


    #for obj in sorted_collections:
        #result += f"-{obj}:\n"
    #return result.strip()












print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany")))
