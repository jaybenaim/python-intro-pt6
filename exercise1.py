the_list = [
{'train': "72C", 'frequency_in_minutes': 15, 'direction': "north"},
{'train': "72D", 'frequency_in_minutes': 15, 'direction': "south"},
{'train': "610", 'frequency_in_minutes': 5, 'direction': "north"},
{'train': "611", 'frequency_in_minutes': 5, 'direction': "south"},
{'train': "80A", 'frequency_in_minutes': 30, 'direction': "east"},
{'train': "80B", 'frequency_in_minutes': 30, 'direction': "west"},
{'train': "110", 'frequency_in_minutes': 15, 'direction': "north"},
{'train': "111", 'frequency_in_minutes': 15, 'direction': "south"}
]

# 1 Save the direction of train 111 into a variable.


for data in the_list: 
    name = data['train']
    if name == '111':
        train_111 = data['direction']

# print(train_111)  

# 2 Save the frequency of train 80B into a variable.
for data in the_list: 
    name = data['train']
    if name == '80B':
        train_80B = data['frequency_in_minutes']
# print(train_80B)
# 3 Save the direction of train 610 into a variable.
for data in the_list: 
    name = data['train']
    if name == '610':
        train_610 = data['direction']
# print(train_610)


# 4 Create an empty list. Iterate through each train and add the name of the train into the list if it travels north.

northbound_trains = [] 

for data in the_list: 
    name = data['train']
    direction = data['direction']
    if direction == 'north':
        northbound_trains.append(name)
# print(northbound_trains)

# 5 Do the same thing for trains that travel east.

northbound_trains = [] 

for data in the_list: 
    name = data['train']
    direction = data['direction']
    if direction == 'north':
        northbound_trains.append(name)
# print(northbound_trains)

eastbound_trains = [] 

for data in the_list: 
    name = data['train']
    direction = data['direction']
    if direction == 'east':
        eastbound_trains.append(name)
# print(eastbound_trains)

# 6 

def direction_of_trains(train_list, direction): 
    for data in train_list: 
        name = data['train']
        train_direction = data['direction']
        if train_direction == direction:
            return name

print(direction_of_trains(the_list, 'east'))
print(direction_of_trains(the_list, 'north'))



# 7 Pick one train and add another key/value pair 
# for the first_departure_time
def dep_time(time): 
    for data in the_list: 
        data['first_departure_time'] = time
    return data['first_departure_time']
    
print(dep_time(3))





























# print(get_value('east'))  
# def key_checker(chosen_value): 
#     for dictionary in the_list: 
#         for key, value in dictionary.items():
#             if value == chosen_value: 
#             # if the value exists print value 
#                 return value
#             else: 
#                 return False 
# def get_value(chosen_key): 
#     for dictionary in the_list: 
#         for key, value in dictionary.items():
#             if value == chosen_key: 
#                 # print(value)
#             # if the value exists print value 
#                 # string = f'{key} {value}'
#                 # return string
#                 # print(string)
#                 for item in the_list: 
#                     for key2, value2 in item.items(): 
#                         # print(key2) 
#                         return the_list[0]# item['train']
#             # else: 
#             #     return False 


# # function 
# # direction and list of trains 
# # returns list of the trains that go in that direction 
# def get_train_direction(direction, train_list): 
#     for train_data  in train_list: 
        
#         for key, value in train_data.items():
#             # if value == direction: 
#             print(train_data['train'])
#                 # print(key)
#             return 
#             # for key2, value2 in   
# get_train_direction("east", the_list)
# #1 Save the direction of train 111 into a variable.
# length = len(the_list) - 1 
# direction_train_11 = the_list[length]['direction']
# #2 Save the frequency of train 80B into a variable.
# frequency_train_80B = get_value('frequency_in_minutes')
# #3 Save the direction of train 610 into a variable.
# direction_train_610 = the_list[2]['direction']
# # print(direction_train_610)

# # Create an empty list. 
# northbound_trains = []
# # Iterate through each train 
# for item  in the_list: 
#     # for train in northbound_trains:
#     for key, value in item.items(): 
#         # if it travels north
#         if value == 'north': 
#             # add the name of the train into the list
#             key_name = get_value('north')
#             northbound_trains.append(key_name)
#             #northbound_trains.append(f'Train: {key_name} is travelling north')


# eastbound_trains = []

# for item  in the_list: 
#     # for train in northbound_trains:
#     for key, value in item.items(): 
#         # if it travels north
#         if value == "east": 
#             key_name = get_value('train') 
#             eastbound_trains.append(key_name)

# # print(northbound_trains)
# # print(eastbound_trains)


   


# #     if train



# frequency = get_value('frequency_in_minutes')

