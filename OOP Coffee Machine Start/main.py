from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
is_on = True
while is_on:
    order = input(f"What would you like to have {menu.get_items()}? ")
    if order == "report":
        coffee_maker.report()
        money_machine.report()
    elif order == "off":
        is_on = False
    else:
        drink= menu.find_drink(order)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)