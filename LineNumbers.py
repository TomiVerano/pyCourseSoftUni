


def count_punctuation_marks(line):
    count_m = int(0)

    numbers = {33, 39, 46, 44, 45, 63}
    for ch in line:
        for i in numbers:
            if ch == chr(i):
                count_m += 1
    return count_m


# Using readlines()
file1 = open("text.txt", "r")
Lines = file1.readlines()

count = 0
# Strips the newline character
for line in Lines:
    count += 1
    letters_count = line.split(" ")
    letters_count_string = "".join(letters_count)
    print("Line{0}: {1}({2})({3})".format(count, line.strip(), (len(letters_count_string) - 1 - count_punctuation_marks(line.strip())), count_punctuation_marks(line.strip())))