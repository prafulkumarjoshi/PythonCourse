import random
print("Welcome to Random Number Generator")

random_number = random.randint(1,10)
print("random_number:", random_number)

ran_num_0_1 = random.random()*10

print("ran_num_0_1:", ran_num_0_1)

h_t = random.randint(0,1)
print("h_t:", h_t)
if h_t == 1:
    print("Heads")
else:
    print("Tails")


state = ["Jammu and kashmir","Delhi"]

friends = ["A", "B", "C", "D", "E", "F"]

print(random.choice(friends))


