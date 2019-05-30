# This code picks a random food item:
from random import choice #DON'T CHANGE!
food = choice(["cheese pizza", "quiche", "morning bun", "gummy bear", "tea cake"]) #DON'T CHANGE!

#DON'T CHANGE THIS DICTIONARY EITHER!
bakery_stock = {
    "almond croissant" : 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25
}

# # YOUR CODE GOES BELOW:
# if food in bakery_stock:
#     print(f"Only {bakery_stock.get(food)} {food} left in jar")
# else:
#     print(f"{food}. We don't make such")

if food in bakery_stock:
    print("{} Only left in jar".format(bakery_stock[food]))
else:
    print("We don't make such")




