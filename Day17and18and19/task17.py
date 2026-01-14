class User:
    def __init__(self, id, name):
        print("New user is being created")
        self.id = id
        self.name = name 
        self.followers = 0
        self.following = 0
        
    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("1", "A")
user_2 = User("2", "B")
user_3 = user_1
user_4 = user_2

print(user_2)
print(user_4.following)

user_1.follow(user_2)

print(user_4.followers)
