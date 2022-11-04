# Program about Dictionaries

car = {"brand":"Ford", "model":"Mustang", "year":1964, "isNew":False}

car["engine"] = "4 Cylinders"
car["colour"] = "white"

print("Original dictionies for car : ", car)

# Add item to car dictionaries here
car["make"] = "Toyota"
print("Dictionaries car after adding make : ", car)

# Update item to car dictionaries here
car["colour"] = "black"
print("Dictionaries car after updating the color : ", car)

# Del item to car dictionaries here

# Loop through the car dictionaries below
for key, value in car.items():
    print(f'{key} : {value}')