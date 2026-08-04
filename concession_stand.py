menu={"pizza": 10,
       "burger": 8,
         "salad": 6,
         "soda": 2,
         "pasta": 12}
cart=[]
total=0
print("-----------MENU-----------")
for key,value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("--------------------------")
while True:
    food=input("select an item(q to quit:").lower()
    if food=="q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
print("-----------CART-----------")
for food in cart:
    total+=menu.get(food)
    print(food,end=" ")
print()
print(f"total is:${total:.2f}")
