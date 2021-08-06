from collections import namedtuple

yes_ans = ["y", "Y", "Yes", "yes"]


class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def to_string(self):
        return self.name, self.email


class CoffeeShop:
    profit = 0
    drink_price = 3
    record = []

    def purchase_coffee(self, num_drinks, person):
        if num_drinks > 0:
            total_cost = self.drink_price * num_drinks
            Receipt = namedtuple("Receipt", ['person', 'num_drinks', 'total_cost'])
            self.profit = self.profit + total_cost
            self.record.append(Receipt(person, num_drinks, total_cost))


if __name__ == "__main__":
    my_shop = CoffeeShop()
    matt = Person("Matt F", "test@test.com")

    done = False

    while not done:
        ans = input("Are there any customers left?: ")
        if ans in yes_ans:
            name = input("Hello, please enter your name: ")
            email = input("Please enter your email: ")
            customer = Person(name, email)
            ans = input(f"Welcome {name}, would you like some coffee?: ")
            if ans in yes_ans:
                num_drinks = input("Mhmm yes indeed, how many drinks?: ")
                num_drinks = int(num_drinks)
                my_shop.purchase_coffee(num_drinks, customer)
                print(f"Your total cost was: {my_shop.record[len(my_shop.record) - 1].total_cost}")
        else:
            done = True

    print("\n\nTodays Record:\n")
    for i in my_shop.record:
        print(f"\nCustomer: {i.person.to_string()}\nDrinks Purchased: {i.num_drinks}\nTotal: {i.total_cost}")

    print("-" * 20)
    print(f"Total Money Made: {my_shop.profit}")
