MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 1000,
    "milk": 2000,
    "coffee": 100,
}

#TODO : 4. Check if the amount is sufficient for the order.
def check_amount(order_item, amount):
    required_for_order = MENU[order_item]['cost']
    if amount < required_for_order:
       return f"Insufficient money for the order. Amount ${amount} refunded."
    change = round(amount - required_for_order, 2)
    if amount > required_for_order:
        return f"Change ${change} returned. "
def check_current_resources(c_res, order_name):
    for item in c_res:
        if c_res[item] < MENU[order_name]['ingredients'][item]:
            print(f"Insufficient {item}")
            return False
        else:
            return True
balance = 0
#TODO : 1. Ask user their order.
should_continue = True
while should_continue:

    order = input("What would you like to have: espresso/ latte/ cappuccino?: ").lower()
    if order == 'report':
        for key, value in resources.items():
            print(f"{key}: {value}")
        should_continue = False
    if order == 'off':
        print("Machine turning off.....")
        should_continue = False
    #TODO : 5. Deduct resources for the order from the available supplies.
    if order in MENU:
        if not check_current_resources(resources, order):
            should_continue= False
        resources.update({"water": resources['water']- MENU[order]['ingredients']['water']})
        resources.update({"milk": resources['milk'] - MENU[order]['ingredients']['milk']})
        resources.update({"coffee": resources['coffee']- MENU[order]['ingredients']['coffee']})
        balance = MENU[order]['cost']
        resources['balance'] = balance

    #TODO : 2. Ask user to insert coins.

        coins = {'quarters': 0.25, 'dimes': 0.10, 'nickles': 0.05, 'pennies': 0.01}
        print("Insert coins>>")
        quarters = int(input("Insert quarters: "))
        dimes = int(input("Insert dimes: "))
        nickles = int(input("Insert nickles: "))
        pennies = int(input("Insert pennies: "))

        #TODO : 3. Calculate the total value of coins inserted.
        total = (quarters * coins['quarters']) + (dimes * coins['dimes']) + (nickles * coins['nickles']) + (pennies * coins['pennies'])
        rounded_total = round(total, 2)
        print(f"You've inserted ${rounded_total} in total.")
        print(check_amount(order, rounded_total))
        print("Your order is processing...")
        print(f"Your cup of {order} is finished. Have a nice day! :)")
        print("\n" * 5)

