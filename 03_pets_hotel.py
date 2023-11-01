from collections import OrderedDict

def accommodate_new_pets(*args):
    accommodation = {}
    hotel_capacity, max_weight, *pet_tuples = args
    result = ""
    #result += str(hotel_capacity) + "\n"
    #result += str(max_weight) + "\n"

    for entry in pet_tuples:
        pet_type, pet_weight = entry
        if pet_weight <= max_weight:
            if pet_type not in accommodation:
                accommodation[pet_type] = []
                if hotel_capacity > 0:
                    accommodation[pet_type].append(pet_weight)
                    hotel_capacity -= 1
            else:
                if hotel_capacity > 0:
                    accommodation[pet_type].append(pet_weight)
                    hotel_capacity -= 1
    if hotel_capacity > 0:
        result += f"All pets are accommodated! Available capacity: {hotel_capacity}.\n"
    else:
        result += "You did not manage to accommodate all pets!\n"
    new_dict = OrderedDict(sorted(accommodation.items()))
    for key, value in new_dict.items():
        result += f"{key}: {len(value)}\n"
    return result



print(accommodate_new_pets( 10, 10.0, ("cat", 5.8), ("dog", 10.5), ("parrot", 0.8), ("cat", 3.1), ))