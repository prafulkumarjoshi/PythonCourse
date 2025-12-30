import random
states = ["Jammu and kashmir","Delhi","Haryana"]

for s in states:
    print(s)

scores = [1,4,556,778,8879,34,21]

print(sum(scores))

print(max(scores))

#find max number in a list of numbers
highest = 0
for s in scores:
    if s > highest:
        highest = s
        
print("Highest: ", highest)

#Range function
sum = 0
for i in range(1,101):
    sum +=i

print(sum)