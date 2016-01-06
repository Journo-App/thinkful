class Customer(object):
    def __init__(self, name, budget=0.0):

        self.name = name
        self.budget = budget

class Bicycle(object):
    def __init__(self, model, weight, prod_cost=0.0):

        self.model = model
        self.weight = weight
        self.prod_cost = prod_cost

    def __str__(self):
        return self.model


class Bikeshop(object):
    def __init__(self, shop_name, inventory):
        self.shop_name = shop_name
        self.inventory = inventory

    def list_bicycles(self):
        for bicycle in self.inventory:
            print (bicycle.prod_cost, bicycle.model)


    def check_budget(self, customer, listOfBikes):
        budget = customer.budget
        can_purchase = []


        for bicycle in listOfBikes:
            real_cost = self.calculate_bike_cost(bicycle)


            if budget >= real_cost:
                can_purchase.append(bicycle) 
                print ("You can buy {} ".format(bicycle.model))

            else:
                print ("You can't buy {} ".format(bicycle.model))

        return can_purchase

    def check_budget_1(self, customer):
        budget = customer.budget

        for bicycle in self.inventory:
            real_cost = calculate_bike_cost(bicycle)

            if budget < real_cost:
                print ("You can not buy {} ".format(bicycle.model))
            else:
                print ("You can buy {} ".format(bicycle.model))


    def calculate_bike_cost(self, Bicycle): 

        return Bicycle.prod_cost * 1.2 


    def print_inventory(self):
        print (self.inventory)

if __name__ == '__main__':

# 1. Have each of the three customers purchase a bike then print the name of the bike the customer purchased
# 2. the cost,
# 3. and how much money they have left over in their bicycle fund.

    bianchi = Bicycle('Bianchi', 6, 450.0)
    schwinn = Bicycle('Schwinn', 10, 100.0)
    abici = Bicycle('Abici', 5, 300.0)
    cinelli = Bicycle('Cinelli', 4, 400.0)
    eagle = Bicycle('Eagle', 6, 200.0)
    falcon = Bicycle('Falcon', 7, 930.0)
    
    bike_list = [bianchi, schwinn, abici, cinelli, eagle, falcon]


    rock_star = Bikeshop(' Rock Star', {'bianchi': 2, 'schwinn': 5, 'abici': 7, 'cinelli': 1, 'eagle': 2, 'falcon': 6})
    # blow_up = Bikeshop('Blow Up', {bianchi: 9, schwinn: 5, abici: 1, cinelli: 1, eagle: 2, falcon: 6})
    # tired = Bikeshop('Tired on Mission', {bianchi: 8, schwinn: 12, abici: 11, cinelli: 10, eagle: 22, falcon: 16} )

    #A list of bikes sold by each bike shop
    rockstar_bikes = rock_star.inventory
    print (rockstar_bikes[schwinn])
    rock_star.inventory[schwinn] -= 1
    print (rock_star.inventory[schwinn])

    blowup_bikes = blow_up.inventory
    print (blowup_bikes[bianchi])
    blow_up.inventory[bianchi] -= 1
    print (blow_up.inventory[bianchi])


    #Create three customers. One customer has a budget of $200, the second $500, and the third $1000.

    ramona = Customer('Ramona', 200.0)
    ramona.budget = 200.0
    ramona.after_budget = ramona.budget - schwinn.real_cost
    rock_star.check_budget(ramona)

    print ("Ramona wants to purchase a", schwinn)
    print ("Ramona's budget is", ramona.budget)
    print ("Ramona's budget after buying the bike is",ramona.after_budget)

    felicia = Customer('Felicia', 500.0)
    rock_star.check_budget(felicia)

# 	annie = Customer('Annie', 1000.0)
# 	cyclery.check_budget(annie)

# #rockstar_bikes = rock_star.list_bicycles
# 	rock_star.list_bicycles()




			
