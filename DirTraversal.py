# import required module
import os

# assign directory
p = ""
directory = input()
all_dir = []
# iterate over files in
# that directory
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        try:
            p = open("report.txt", "w+")
            p.writelines(f)
        except:
            p.close()
        print(print(f))

#no time for more coding :( deadline!!!