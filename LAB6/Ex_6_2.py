import json

# test = [{"name": "Kacper", "age": 22, "gender": "Male"}, {"name": "Adrian", "age": 23, "gender": "Male"}, {"name": "Ola", "age": 21, "gender": "Female"}]
# jsonString = json.dumps(test)
# jsonFile = open("C:/Users/Kacper/Desktop/AGH/7Semester/Python/LAB6/names.json", "w")
# jsonFile.write(jsonString)
# jsonFile.close()

with open("C:/Users/Kacper/Desktop/AGH/7Semester/Python/LAB6/names.json", "r") as open_file:
    json_object = json.load(open_file)

for obj in json_object:
    for key in obj:
        print(key + ": " + str(obj[key]))

    print()

menu_input = input("1 - Add new entry\n"
                   "2 - Delete existing entry\n"
                   "3 - Quit\n")

if menu_input == "1":
    name_input = input("Provide name: ")
    age_input = input("Provide age: ")
    gender_input = input("Provide gender: ")

    person_object = {"name": name_input, "age": age_input, "gender": gender_input}
    json_object.append(person_object)

    jsonString = json.dumps(json_object)
    with open("C:/Users/Kacper/Desktop/AGH/7Semester/Python/LAB6/names.json", "w") as open_file:
        open_file.write(jsonString)

elif menu_input == "2":
    name_input = input("Provide name of the set to be deleted: ")

    for element in json_object:
        if element["name"] == name_input:
            json_object.remove(element)

            jsonString = json.dumps(json_object)
            with open("C:/Users/Kacper/Desktop/AGH/7Semester/Python/LAB6/names.json", "w") as open_file:
                open_file.write(jsonString)

            print("Successfully removed " + name_input + " from the file")


