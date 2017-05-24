# -*- coding: utf-8 -*-
#This is the first program based on the examples given on book 'Data Science From Scratch'
#uncomment the print commands to test the execution flow

#Create a dicrtionary of users
users = [
    {"id":0,"Birth":1984,"name":"Arsh"},
    {"id":1,"Birth":1982,"name":"Air"},
    {"id":2,"Birth":1994,"name":"Alm"},
    {"id":3,"Birth":1991,"name":"Bbu"},
    {"id":4,"Birth":1974,"name":"Rafl"},
    {"id":5,"Birth":1968,"name":"Lana"}
]
#test: print id/name/Birth of each user i users
#for user in users:
#    print("Id:",user["id"])
#    print("Birth year:",user["Birth"])
#    print("Name:",user["name"])
#    print("--------------")

#create a new attribute in users
for user in users:
    user["relatives"] = []     

#relationship list
relationship = [(0,1),(0,2),(0,4),(1,2),(1,5),(2,3),(2,5),(3,5),(4,5)]

#print each relationship pairs and append relationship in users
for i,j in relationship:
    users[i]["relatives"].append(j) # add j as a relative of i
    users[j]["relatives"].append(i) # ass i as a relative of j

#test: relatives
#for user in users:
#    print("Id:",user["id"])
#    print("Relatives:",user["relatives"])
#    print("--------------------------")

#who has the maximum number of relatives
def number_of_relatives(user):
    return len(user["relatives"]) 

#create a list of number of relatives for each user
num_relatives_by_id = [(user["id"],number_of_relatives(user)) for user in users]

#now sort by number of relatives
num_relatives_by_id = sorted(num_relatives_by_id, key = lambda item:item[1], reverse = True)

#test: sorted by number of relatives
for rel in num_relatives_by_id:
    print(rel)  