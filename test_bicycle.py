import unittest
from bicycle import Bikeshop, Customer, Bicycle 

class BicycleTestCase(unittest.TestCase): 


# Create a bicycle shop that has 6 different bicycle models in stock. 
    def test_bikeshop_has_six_models(self):
        rock_star = Bikeshop(' Rock Star', {'bianchi': 2, 'schwinn': 5, 'abici': 7, 'cinelli': 1, 'eagle': 2, 'falcon': 6})
        self.assertEqual(len(rock_star.inventory), 6)


# The shop should charge its customers 20% over the cost of the bikes.

    def test_bikeshop_markup(self):
        
        bianchi = Bicycle('Bianchi', 6, 450.0)
        rock_star = Bikeshop(' Rock Star', {'bianchi': 2, 'schwinn': 5, 'abici': 7, 'cinelli': 1, 'eagle': 2, 'falcon': 6})

        self.assertEqual (rock_star.calculate_bike_cost(bianchi), 450 * 1.2) 


# One customer has a budget of $200, the second $500, and the third $1000.
    
    def test_customer_budget(self):

        ramona = Customer('Ramona', 200.0)
        felicia = Customer('Felicia', 500.0)
        annie = Customer('Annie', 1000.0)
        
        self.assertEqual(ramona.budget, 200)
        self.assertEqual(felicia.budget, 500)
        self.assertEqual(annie.budget, 1000)


#Check customer's budget against the cost of each bike to make sure they can afford at least one bike

#figure out why py.test indentation error ********

    def test_customer_can_afford_a_bike(self):
        ramona = Customer(name='Ramona', budget=200.0)
        rock_star = Bikeshop(' Rock Star', {'bianchi': 2, 'schwinn': 5, 'abici': 7, 'cinelli': 1, 'eagle': 2, 'falcon': 6})
        bianchi = Bicycle('Bianchi', 6, 450.0)
        schwinn = Bicycle('Schwinn', 10, 100.0)
        abici = Bicycle('Abici', 5, 300.0)
        cinelli = Bicycle('Cinelli', 4, 400.0)
        eagle = Bicycle('Eagle', 6, 200.0)
        falcon = Bicycle('Falcon', 7, 930.0)
        bike_list = [bianchi, schwinn, abici, cinelli, eagle, falcon]

        # if ramona.budget >= rock_star.calculate_bike_cost(bianchi): 
        #   return True 
        # else: 
        #   return False 
        self.assertEqual(len(rock_star.check_budget(ramona, bike_list)), 1)
        #self.assertEqual(len(rock_star.check_budget(felicia, bike_list)), 4)


if __name__ == '__main__':
    unittest.main()
