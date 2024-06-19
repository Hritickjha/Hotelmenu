# Define the menu of restaurant
menu = {
    'pizza' : 50,
    'Burger': 80,
    'Chowemin' : 100,
    'samosa' : 80,
    'pani puri' : 50,
    'cold drink' : 45,
}
# Greet
print("welcome to Cyber Restaurant")
print("pizza: Rs50\nBurger: Rs80\nChowemin: Rs100\nsamosa: Rs80\npani puri: Rs50\ncold drink: Rs45")

order_total = 0

item_1 = input("Enter the name of item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"your item {item_1} has been added to your order")
else:
    print(f"ordered item {item_1} is not available yet!")
another_order  = input ("Do you want to add another item? (yes/No)")
if another_order == "yes":
    item_2 = input("Enter the name of second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to order")
    else: 
        print(f"order item {item_2} is not availabe! ")
        
print(f"The total amout of items to pay is {order_total}")  
   