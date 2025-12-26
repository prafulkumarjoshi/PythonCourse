# import random as rd

# curr_movies={'LOL':"Laugh Out Loud", 'BFF':"Best Friend"}

# for key in curr_movies:
#     print(key)
#     print(curr_movies[key])
#     print(curr_movies.get(key))


# user_input = input("What movie?\n")

import requests
response =  requests.get('http://api.open-notify.org/astros.json')

json = response.json()

print(json)

for p in json['people']:
     print(p['name'])