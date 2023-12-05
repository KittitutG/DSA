initial_dictionary = {
        "one": 1,    
        "two": 2,
       }
initial_dictionary["three"] = 3
final_dict = initial_dictionary
print(final_dict)

print('-----------')
custom_dict = {
        "one": 1,    
        "two": 2,    
        "three": 3,
    }
# print(custom_dict[2])

print('------------')
order = {
    "starter": {1: "Salad", 2: "Soup"},    
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},    
    "dessert": {1: ["Ice Cream"], 2: []},
}
print(order["main"][1][0])