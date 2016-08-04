class Customer(object):
    def __init__(self, name, budget=0.0):
        self.name = name
        self.budget = budget


class Bicycle(object):
    def __init__(self, model, weight, cost=0.0):

        self.model = model
        self.weight = weight
        self.cost = cost

    def __str__(self):
        return "Model:%s , Weight:%s, Cost:%s " % (self.model, self.weight, self.cost)


class Bikeshop(object):
    def __init__(self, shop_name, inventory):
        self.shop_name = shop_name
        self.inventory = inventory

    def list_bicycles(self):
        for bicycle in self.inventory:
            print (bicycle.cost, bicycle.model)

    def check_budget(self, customer):
        budget = customer.budget

        for bicycle in self.inventory:
            real_cost = bicycle.cost * .20 + cost
            if budget < real_cost:
                print ("You can not buy {} ".format(bicycle.model))
            else:
                print ("You can buy {} ".format(bicycle.model))

    def print_inventory(self):
        print (self.inventory)


if __name__ == '__main__':
    
    bianchi = Bicycle(model='Bianchi', weight=6, cost=450.0)
    schwinn = Bicycle(model='Schwinn', weight=10, cost=100.0)
    abici = Bicycle(model='Abici', weight=5, cost=300.0)
    cinelli = Bicycle(model='Cinelli', weight=4, cost=400.0)
    eagle = Bicycle(model='Eagle', weight=6, cost=200.0)
    falcon = Bicycle(model='Falcon', weight=7, cost=930.0)


ramona = Customer(name='Ramona', budget=200.0)
ramona.after_budget = ramona.budget - schwinn.cost * .20 + schwinn.cost
# schwinn.check_budget(ramona)

print ("Ramona wants to purchase a", schwinn)
print ("Ramona's budget is", ramona.budget)
# print ("Ramona's budget after buying the bike is",ramona.after_budget)

    
