# -*- coding: utf-8 -*-
"""
Created on Wed May 24 15:21:39 2017

@author: malam
"""
from collections import defaultdict
# THIS PROGRAM IS PERFORMS TWO TASKS: 
#    1. TASK IS TO FIND FRIEND OF A FRIEND WHO IS NOT IN THE FRIEND LIST
#    2. FIND COMMON INTEREST BEWTEEN THE EMPLOYEES OF AN ORGANIZATION
# NOTE: users dictionary and friendship list are copied from Data Science from Scratch book 
# Create a dicrtionary of users
users = [
        { "id": 0, "name": "Hero" },
        { "id": 1, "name": "Dunn" },
        { "id": 2, "name": "Sue" },
        { "id": 3, "name": "Chi" },
        { "id": 4, "name": "Thor" },
        { "id": 5, "name": "Clive" },
        { "id": 6, "name": "Hicks" },
        { "id": 7, "name": "Devin" },
        { "id": 8, "name": "Kate" },
        { "id": 9, "name": "Klein" }
        ]
#List of companies
company = [(1,"IBM"),(2,"Google"),(3,"Microsoft")]
#List of companies they work(ed) for 
employer = [(0,1),(1,2),(2,2),(3,3),(4,2),(5,3),(6,3),(7,3),(8,1),(9,1)]
#interests list
interests = [
            (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
            (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
            (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
            (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
            (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
            (3, "statistics"), (3, "regression"), (3, "probability"),
            (4, "machine learning"), (4, "regression"), (4, "decision trees"),
            (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
            (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
            (6, "probability"), (6, "mathematics"), (6, "theory"),
            (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
            (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
            (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
            (9, "Java"), (9, "MapReduce"), (9, "Big Data")
            ]
# List of friendships between the users
friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
               (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]
#Additional attributes to users
for user in users:
    user["friends"] = []
    user["companyID"] = []
    user["interests"] = []
#Friendship network
#please note if .append(i) is used then only user id will be saved which can not be indexed
#users[j] saves user object which can be indexed later if needed
for i,j in friendships:
    users[i]["friends"].append(users[j]) # append user j as a friend of user i
    users[j]["friends"].append(users[i]) # append user i as a friend of user j

#Employer ID
for i,j in employer:
    users[i]["companyID"].append(j) # append j as a relative of i
    #users[j]["companyID"].append(i) # append i as a relative of j
#Interests
for i,j in interests:
    users[i]["interests"].append(j) # append j as interests of i
#display user details
#for user in users:
#    print(user)
#------------------------------------------------------------------------------
#PROBLEM1: FRIEND OF A FRIEND WHO IS NOT IN THE FRIEND LIST OF A USER
new_fl = []  
   
def not_repeated(cur_list,foaf_list):
    for foaf_l in foaf_list:
        return cur_list != foaf_l["id"]  

def friends_of_friend_ids(user):
    ## "foaf" is short for "friend of a friend"
    #for usr in user["friends"]:
    #    print(usr["id"]) 
    return [new_fl.append(foaf["id"]) 
            for friend in user["friends"] # for each of user's friends
            for foaf in friend["friends"] # get each of _their_ friends
            if not_repeated(foaf["id"],user["friends"]) # To find unknown friends
            and foaf["id"] not in new_fl
            ] 

friends_of_friend_ids(users[1])
print(new_fl) #print the list of foaf
#------------------------------------------------------------------------------
#PROBLEM2: COMMON INTERESTS BETWEEN THE EMPLOYEES OF AN ORGANIZATION

user_ids_by_company = defaultdict(list) #list of users in each company
for user_id, company in employer:
    user_ids_by_company[company].append(user_id)

company_interests = [] 
def get_interests(user_list):
    return [company_interests.append(j) 
            for i in user_list
            for j in users[i]["interests"]
            if j not in company_interests
            ]

get_interests(user_ids_by_company[2]) #get interests in company x
print(company_interests)



   