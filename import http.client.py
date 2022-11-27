import http.client

conn = http.client.HTTPSConnection("nutritionix-api.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "8249f77f64msh0340c24930fb03ap11c7dbjsnb0e487646a16",
    'X-RapidAPI-Host': "nutritionix-api.p.rapidapi.com"
    }

# This block of code is to test different foods
askFood = input("Enter a food: ")
"""
word = ""
space_index = askFood.find(" ")
if space_index != 0:
    word += askFood[0 : space_index] + str("%20") + askFood[space_index + 1:]
    askFood = askFood[space_index + len("%20"):]
    spaceIndex = askFood.find(" ")
"""
word = ""
if askFood.find(" ") != 0:
    word = askFood.replace(" ", "%20")

conn.request("GET", "/v1_1/search/" + str(word) + "?fields=item_name%2Cnf_calories%2Cnf_total_fat", headers=headers)

res = conn.getresponse()
data = res.read()

information = data.decode("utf-8")
information2 = information
information3 = information
information4 = information

arr_item_name = []
count = 0
index_item_name = information.find("item_name")

while (index_item_name != 0):
   name_of_item = information[index_item_name + len("item_name") + 3: index_item_name + len("item_name") + 3 + information[index_item_name + len("item_name") + 3:].find("nf_calories") - 3]
   arr_item_name.append(name_of_item)
   information = information[index_item_name + len("item_name") + 3:]
   index_item_name = information.find("item_name")
   if count == 9:
       break
   else:
       count = count + 1
print("The array is", arr_item_name)

arr_calories = []
count2 = 0
index_calories = information2.find("nf_calories")
while(index_calories != 0):
    num_of_calories = information2[index_calories + len("nf_calories") + 2: index_calories + len("nf_calories") + 2 + information2[index_calories + len("nf_calories") + 2:].find("nf_total_fat") - 2]
    arr_calories.append(num_of_calories)
    information2 = information2[index_calories + len("nf_calories") + 2:]
    index_calories = information2.find("nf_calories")
    if count2 == 9:
       break
    else:
       count2 = count2 + 1
print("The array is", arr_calories)

arr_serving_size = []
count4 = 0
index_serving_size = information4.find("nf_serving_size_qty")
while index_serving_size != 0:
    num_serving_size = information4[index_serving_size + len("nf_serving_size_qty") + 2: index_serving_size + len("nf_serving_size_qty") + 2 + information4[index_serving_size + len("nf_serving_size_qty") + 2:].find("nf_serving_size_unit") - 2]
    arr_serving_size.append(num_serving_size)
    information4 = information4[index_serving_size + len("nf_serving_size_qty") + 2:]
    index_serving_size = information4.find("nf_serving_size_qty")
    if count4 == 9:
        break
    else:
        count4 = count4 + 1
print("The array is", arr_serving_size)

arr_fat = []
count3 = 0
index_total_fat = information3.find("nf_total_fat")
while index_total_fat != 0:
    num_total_fat = information3[index_total_fat + len("nf_total_fat") + 2: index_total_fat + len("nf_total_fat") + 2 + information3[index_total_fat + len("nf_total_fat") + 2:].find("nf_serving_size_qty") - 2]
    arr_fat.append(num_total_fat)
    information3 = information3[index_total_fat + len("nf_total_fat") + 2:]
    index_total_fat = information3.find("nf_total_fat")
    if count3 == 9:
        break
    else:
        count3 = count3 + 1
print("The array is", arr_fat)

"""
# This block of code finds the number of total fat in a food from API
index_total_fat = information3.find("nf_total_fat")
num_of_total_fat = information3[index_total_fat + len("nf_total_fat") + 2: index_total_fat + len("nf_total_fat") + 2 + information3[index_total_fat + len("nf_total_fat") + 2:].find("nf_serving_size_qty") - 2]
print(num_of_total_fat)

# This block of code finds the serving size in a food from API
index_serving_size = information4.find("nf_serving_size_qty")
num_serving_size = information4[index_serving_size + len("nf_serving_size_qty") + 2: index_serving_size + len("nf_serving_size_qty") + 2 + information4[index_serving_size + len("nf_serving_size_qty") + 2:].find("nf_serving_size_unit") - 2]
print(num_serving_size)

# This block of code finds the number of calories in a food from API
index_calories = information2.find("nf_calories")
num_of_calories = information2[index_calories + len("nf_calories") + 2: index_calories + len("nf_calories") + 2 + information2[index_calories + len("nf_calories") + 2:].find("nf_total_fat") - 2]
print(num_of_calories)

# This block of code finds the item names in a food from API 
index_item_name = information.find("item_name")
name_of_item = information[index_item_name + len("item_name") + 3: index_item_name + len("item_name") + 3 + information[index_item_name + len("item_name") + 3:].find("nf_calories") - 3]
if name_of_item.find("\\\"") != 0:
    name_of_item = name_of_item[0 : name_of_item.find("\\\"")] + name_of_item[name_of_item.find("\\\"") + 2:]
print(name_of_item)

"""












#for i in range(len(information)):
    #index = information.find("item_name")
    #new_information = information[index + len("item_name")]
    
    
    


