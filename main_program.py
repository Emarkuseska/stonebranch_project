from find_data_func import find_data
while True:
    print("If you want to stop the program input 0 ")
    print(r"Write the name of the fist database with .csv, or the path in this format r'C:\docs\data.csv'")
    name1 = input("Write the first name:")
    if name1 == str(0):
        break
    name2 = input("Write the second name:")
    if name2 == str(0):
        break
    find_data(name1, name2)
