class Bicycle(object):
	def __init__(self, model, weight, prod_cost=0.0): 

	    self.model = model
	    self.weight = weight
	    self.prod_cost = prod_cost
	    self.real_cost = prod_cost * .20 + prod_cost


#***charge customers 20% over the cost of the bikes

class Bikeshop(object):
	def __init__(self, shop_name, inventory): 
	    self.shop_name = shop_name
	    self.inventory = inventory
	    
		#self.profit = 0

	def list_bicycles(self):
		for item in self.inventory:
			print (item.prod_cost, item.model)


	def check_budget(self, customer):
		budget = customer.budget
		
		for item in self.inventory:
			real_cost = item.real_cost
			if budget < real_cost:
				print ("you can not buy {} ".format(item.model))
			else:
				print ("*** you can buy {} ".format(item.model))
	    


	def print_inventory(self):
		print (self.inventory) 

#bikestore and inventory 


#Print the initial inventory of the bike shop for each bike it carries.


class Customer(object): 
	def __init__(self, name, budget=0.0): 

		self.name = name
		self.budget = budget
		#self.balance = balance



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

	rock_star = Bikeshop('Rock Star bikes', {bianchi.model: 4, schwinn.model: 3, abici.model: 2, cinelli.model: 4, eagle.model: 2, falcon.model: 6})
	cyclery = Bikeshop('The Cyclery', {bianchi.model: 2, schwinn.model: 5, abici.model: 7, cinelli.model: 1, eagle: 2, falcon: 6})
	blow_up = Bikeshop('Blow Up', {bianchi.model: 9, schwinn.model: 5, abici.model: 1, cinelli.model: 1, eagle: 2, falcon: 6})
	tired = Bikeshop('Tired on Mission', {bianchi.model: 8, schwinn.model: 12, abici.model: 11, cinelli.model: 10, eagle.model: 22, falcon.model: 16} )

	#A list of bikes sold by each bike shop
	rockstar_bikes = rock_star.inventory
	print (rockstar_bikes[schwinn.model])
	rock_star.inventory[schwinn.model] -= 1 
	print (rock_star.inventory[schwinn.model])

	cyclery.print_inventory()

	blow_up.print_inventory()

	tired.print_inventory()

	cyclery.list_bicycles()

	#Create three customers. One customer has a budget of $200, the second $500, and the third $1000.

	ramona = Customer('Ramona', 200.0)
	ramona.budget = 200.0
	ramona.after_budget = ramona.budget - schwinn.real_cost
	rock_star.check_budget(ramona)
	
	print ("ramona wants to purchase a", schwinn.model)
	print ("ramona budget", ramona.budget)
	print ("ramona budget after purchase",ramona.after_budget)

	felicia = Customer('Felicia', 500.0)
	cyclery.check_budget(felicia)

	annie = Customer('Annie', 1000.0)
	cyclery.check_budget(annie)

# #rockstar_bikes = rock_star.list_bicycles
# 	rock_star.list_bicycles()

			
