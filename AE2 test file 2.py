import csv

with open("data/sol_data1.csv") as f1:
    f1.readline()
    for line in f1:
        print(line.split(",")[14])

python_file = open("data\sol_data1.csv", "a")
python_file.write(' ')
python_file.close()