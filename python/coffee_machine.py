# 3 drinks, espresso, latte, cappuccino

# coin operated, penny, nickel, dime, quarter

# machine starts out with resources (water, milk, coffee)

# 1. report command displays resources + money
# 2. Check if machine has sufficient resources
# 3. Insert coins, give change, return drink
#   If not enough money, return money
# 4. Check if transaction is successful

class Menu:
    def __init__(self):
        self.items = {
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
    
    def get_item_ingredients(self, item):
        return self.items[item]['ingredients']

    def get_item_cost(self, item):
        return self.items[item]['cost']


class CoffeeMachine:
    def __init__(self, water=300, milk=200, coffee=100):
        self.resources = {
            'water': water,
            'milk': milk,
            'coffee': coffee
        }

        self.menu = Menu()
        self.money = 0
        self.on = True

    def turn_off(self):
        self.on = False

    def is_on(self):
        return self.on

    def prompt_user(self):
        commands = [
            'espresso',
            'cappuccino',
            'latte',
            'off',
            'report'
        ]

        command = None
        while command not in commands:
            command = input("What would you like? (espresso/latte/cappuccino): ").lower()

        return command

    def execute_command(self, command):
        if command == 'report':
            self.print_report()
        elif command == 'off':
            self.turn_off()
        else:
            drink = command
            if self.has_enough_resources(drink):
                money = self.process_coins()
                if self.has_enough_money(drink, money):
                    self.complete_transaction(drink, money)
                    self.make_drink(drink)
                else:
                    print("Sorry, that's not enough money. Money refunded.")

    def print_report(self):
        print(f'Water: {self.resources["water"]}ml')
        print(f'Milk: {self.resources["milk"]}ml')
        print(f'Coffee: {self.resources["coffee"]}g')
        print(f'Money: ${self.money}')

    def has_enough_resources(self, drink):
        ingredients = self.menu.get_item_ingredients(drink)

        for ingredient in ingredients:
            if self.resources[ingredient] < ingredients[ingredient]:
                print(f'Sorry, there is not enough {ingredient}')
                return False
        return True

    def process_coins(self):
        quarters = self.request_number_of_coins('quarters')
        dimes = self.request_number_of_coins('dimes')
        nickels = self.request_number_of_coins('nickels')
        pennies = self.request_number_of_coins('pennies')
        return (quarters*0.25) + (dimes*0.10) + (nickels*0.05) + (pennies*0.01)

    @staticmethod
    def request_number_of_coins(coins):
        return float(input(f'How many {coins}?: '))

    def has_enough_money(self, drink, money):
        return money >= self.menu.get_item_cost(drink)

    def complete_transaction(self, drink, money):
        drink_cost = self.menu.get_item_cost(drink)
        change = round(money - drink_cost, 2)
        if change > 0:
            print(f'Here is ${change} dollars in change.')
        self.money += drink_cost

    def make_drink(self, drink):
        ingredients = self.menu.get_item_ingredients(drink)
        for ingredient in ingredients:
            self.resources[ingredient] -= ingredients[ingredient]
        print(f'Here is your {drink}. Enjoy!')


def main():
    cm = CoffeeMachine()

    while cm.is_on():
        command = cm.prompt_user()
        cm.execute_command(command)


if __name__ == "__main__":
    main()