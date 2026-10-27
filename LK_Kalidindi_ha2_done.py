#-------------------------------------------------------------------------------
# HA2
# Student Name: LK Kalidindi
# Python version: 
# Submission Date: 10/15/2026
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines as set forth by the
# instructor and the class syllabus.
#-------------------------------------------------------------------------------
# References: 
#-------------------------------------------------------------------------------
# Notes to grader: 
#-------------------------------------------------------------------------------
# Source code below
#-------------------------------------------------------------------------------

#define AddToCart class - a subclass of list class
# making a class called AddToCart
class AddToCart(list): # making a list in the parameter
    # making a function of subtotal
    def subtotal(self):
        # making the total 0
        total = 0
        # making the for loop called burger
        for burger in self:
            # making the total equation
            total += burger.get_price()
        return round(total, 2)# making the return statment 

    # making the tax function
    def tax(self):
        return round(self.subtotal() * 0.0325, 2)

    # making the total function
    def total(self):
        return round(self.subtotal() + self.tax(), 2)


#define SimpleBurger class
class SimpleBurger(object):
    cart = AddToCart() #class variable
    simple_burger_price = {'single': 7.99, 'double': 10.99} #class variable
    #Your Code Here
    # making the function with self and the ingredents
    def __init__(self, bun, patty):
        # making the self of the ingredents
        self.bun = bun # the bun
        # making the patty
        self.patty = patty
        #making the cart append of simpleBurger
        SimpleBurger.cart.append(self)

    # making the function of getting price
    def get_price(self):
        return SimpleBurger.simple_burger_price[self.patty]

    # making the str of the self
    def __str__(self):
        return f"{self.bun}-{self.patty}-{self.get_price():.2f}"


#define Subclasses
class CheeseBurger(SimpleBurger):
    cheese_type_price = {'american': 1.99, 'pepper jack': 0.99} #aditional price on base price
    #Your code here
    #define VeggieBurger subclass
    def __init__(self, bun, patty, cheese_type):
        # making the super statment
        super().__init__(bun, patty)
        # making the self statment of the type of cheese
        self.cheese_type = cheese_type

    #making the function of getting price
    def get_price(self):
        # making the base with the super of get price
        base = super().get_price()
        return round(base + CheeseBurger.cheese_type_price[self.cheese_type], 2)

    # making the str of the self
    def __str__(self):
        # making the return statment of the ingredents
        return f"{self.bun}-{self.patty} with {self.cheese_type}-{self.get_price():.2f}"


# making a class called a item from the menu which is VeggieBurger
class VeggieBurger(SimpleBurger):
    veggie_type_price = {'lettuce': 0.99, 'tomato': 0.99, 'caramelized onion': 2.99}

    def __init__(self, bun, patty, veggie_type):
        super().__init__(bun, patty)
        self.veggie_type = veggie_type

    def get_price(self):
        base = super().get_price()
        return round(base + VeggieBurger.veggie_type_price[self.veggie_type], 2)

    def __str__(self):
        return f"{self.bun}-{self.patty} with {self.veggie_type}-{self.get_price():.2f}"


#-------------------------------- 
#main function/global code
#take user input on Burger type
#create object depending on type
choice = ''
print('******** Welcome to 209 Burger ******** \n\n')

while choice!='no':
    burger_type = input('\tEnter type of Burger(simple/cheese/veggie): ')
    # one of the ingredents in the food
    bun = input('\tEnter bun type (white/wheat): ').lower()

    # the patty ingredent
    patty = input('\tEnter patty count (single/double): ').lower()

    # creating the object depending on type
    if burger_type.lower() == 'simple':
        SimpleBurger(bun, patty)

    elif burger_type.lower() == 'cheese':
        cheese_type = input('\tEnter cheese type (american/pepper jack): ').lower()
        CheeseBurger(bun, patty, cheese_type)

    elif burger_type.lower() == 'veggie':
        veggie_type = input('\tEnter veggie topping (lettuce/tomato/caramelized onion): ').lower()
        VeggieBurger(bun, patty, veggie_type)

    # asking user to continue ordering
    choice = input('\tDo you want to continue ordering (yes/no): ').lower()


#Print receipt
#calculate subtotal, tax and total.
print('\n\n\t******** Printing Receipt *******\n')

# making a for loop of the burget
for index, burger in enumerate(SimpleBurger.cart):
    # making print statment
    print(f"{index}-")
    print(burger)

# printing the statment of the subtotal
print(f"\nSubtotal: {SimpleBurger.cart.subtotal():.2f}")
# printing the tax 
print(f"Tax: {SimpleBurger.cart.tax():.2f}")
# printing the total
print(f"Total: {SimpleBurger.cart.total():.2f}")

# printing the thanks message
print("\nThanks for coming!")
