dict = {"A":1, "B":2}

print(dict["B"])

dict["C"]=3

print(dict)

for item in dict:
    print(item, dict[item])
    
state_capitals = {"Karnataka":"Bengaluru","Maharashtra":"Mumbai"}

state_cities = {"Karnataka":["Bengaluru","Hubli","Belagavi"],"Maharashtra":["Mumbai","Pune","Nagpur"]}

print(state_cities["Karnataka"][1])

nested_list = [1,2,[3,4]]

print(nested_list[2][1])
