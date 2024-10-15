import csv


user_pet_input = input("Cat or Dog?: ")
if user_pet_input.lower() == "cat":
    cat_file = "./data/cats.csv"
    cat_info = []
    with open(cat_file, 'r', newline = "") as cat:
        reader = csv.reader(cat)
        for row in reader:
            cat_info.append(row)
    for cat in cat_info[1:]:
        print(f"{cat[0]} is a{cat[1]} year old{cat[2]}")

elif user_pet_input.lower() == "dog":
    dog_info = []
    with open("./data/dogs.csv", 'r', newline = "") as dog:
        reader = csv.reader(dog)
        for row in reader:
            dog_info.append(row)
    for dog in dog_info[1:]:
        print(f"{dog[0]} is a{dog[1]} year old{dog[2]}")
else:
    raise Exception(f"Sorry, we don't have any {user_pet_input} here.")
    

    