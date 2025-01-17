dict1 = {"color": "black", "type": "keyboard", "brand": "Logitech"}
dict2 = {"color": "white", "type": "mouse", "brand": "Razer"}
dict3 = {"color": "silver", "type": "laptop", "brand": "Dell"}
dict4 = {"color": "gray", "type": "monitor", "brand": "Samsung"}
dict5 = {"color": "blue", "type": "headphones", "brand": "Sony"}

dict_list = [dict1, dict2, dict3, dict4, dict5]

print("All keys using Method 1:")
for d in dict_list:
    print(d.keys())  # Method 1: .keys() method

print("\nAll keys using Method 2:")
for d in dict_list:
    for key in d:  
        print(key)

print("\nAll values using Method 1:")
for d in dict_list:
    print(d.values())  # Method 1: .values() method

print("\nAll values using Method 2:")
for d in dict_list:
    for value in d.values():  # Method 2: iterating over .values()
        print(value)

print("\nAll values using Method 3:")
for d in dict_list:
    for key in d:  # Method 3: accessing value with each key
        print(d[key])

print("\nDescriptive sentences based on each dictionary:")
print("Color of this " + dict1["type"] + " is " + dict1["color"] + " and brand is " + dict1["brand"] + ".")
print("Color of this " + dict2["type"] + " is " + dict2["color"] + " and brand is " + dict2["brand"] + ".")
print("Color of this " + dict3["type"] + " is " + dict3["color"] + " and brand is " + dict3["brand"] + ".")
print("Color of this " + dict4["type"] + " is " + dict4["color"] + " and brand is " + dict4["brand"] + ".")
print("Color of this " + dict5["type"] + " is " + dict5["color"] + " and brand is " + dict5["brand"] + ".")
