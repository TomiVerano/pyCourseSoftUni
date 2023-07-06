countries = input().split(", ")
capitals = input().split(", ")

join_dict = {countries[index]: capitals[index] for index in range(len(countries))}

for country, capital in join_dict.items():
    print(f"{country} -> {capital}")