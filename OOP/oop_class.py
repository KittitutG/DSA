class StarCookie:
    milk = 0.5
    def __init__(self,color,weight): #given initializa protperties
        self.color = color
        self.weight = weight


star_cookie1 = StarCookie('red',15)

print(star_cookie1.weight)
print(star_cookie1.color)

print(star_cookie1.__dict__) #get all available properties

'''
default value for properties
'''
# class Youtube:
#     def __init__(self,username,subscribers=0) -> None: #default properties with 0
#         self.username = username
#         self.subscribers = subscribers

# user1 = Youtube("KG")
# print(user1.username)
# print(user1.subscribers)
# user1.subscribers = 15
# print(user1.subscribers)
