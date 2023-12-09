class Youtube:
    def __init__(self,username,subscribers=0,subscriptions=0) -> None: #default properties with 0
        self.username = username
        self.subscribers = subscribers
        self.subscriptions = subscriptions
    def subscribes(self,user):
        self.subscriptions +=1 #our subscripe channel got increase by 1
        user.subscribers +=1 #target channel has 1 more follwer 


user1 = Youtube('Kittitut')
user2 = Youtube('Tae')

print('------------------------')
print('intial status')
print(f"User 1 subscription: {user1.subscriptions}")
print(f"User 1 follower: {user1.subscribers}")
print(f"User 2 subscription: {user2.subscriptions}")
print(f"User 2 follower: {user2.subscribers}")

print('------------------------')
print("User 1 follow User2")
user1.subscribes(user2)
print(f"User 1 subscription: {user1.subscriptions}")
print(f"User 1 follower: {user1.subscribers}")
print(f"User 2 subscription: {user2.subscriptions}")
print(f"User 2 follower: {user2.subscribers}")

print('------------------------')
print("User 2 follow User1")
user2.subscribes(user1)
print(f"User 1 subscription: {user1.subscriptions}")
print(f"User 1 follower: {user1.subscribers}")
print(f"User 2 subscription: {user2.subscriptions}")
print(f"User 2 follower: {user2.subscribers}")
