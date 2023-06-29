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
profit=0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def select_flavours(ingredients):
        # Check resources
    is_enough= True
    for key in ingredients:
        if ingredients[key] < resources[key]:
            resources[key] -= ingredients[key]
        elif ingredients[key] >= resources[key]:
            print(f"Sorry there is not enough {key}.")
            is_enough=False
    return is_enough

def coins_check():
    quarters= int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total_given_amount=quarters*0.25 + dimes* 0.10 + nickles*0.05 + pennies* 0.01

    return total_given_amount

def transaction_succesfully(total_given_amount,cost_coffee):
    # cost_coffee=MENU[flavours]["cost"]
    if total_given_amount>=cost_coffee :
        change = round(total_given_amount - cost_coffee,2)
        print(f"Here is ${change} dollars in change.")
        print(f"after purchasing report {resources} ")
        print(f"“Here is your {flavours}. Enjoy!”.")
        global profit
        profit+= cost_coffee
        return True
    else:
        print(f"Sorry that's not enough money.{total_given_amount} Money refunded.")
        return False

should_stop_noingredient = True
while should_stop_noingredient:
    flavours = input("What would you like? (espresso/latte/cappuccino):")
    # ingredients = MENU[flavours]["ingredients"]
    if flavours == "off":
        should_stop_noingredient = False
    elif flavours == "report":
        # print(f"Before purchasing latte:")
        print(f"Water : {resources['water']}ml")
        print(f"Milk : {resources['milk']}ml")
        print(f"Coffee : {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink= MENU[flavours]
        if select_flavours(drink['ingredients']):
            payment=coins_check()
            transaction_succesfully(payment,drink['cost'])


