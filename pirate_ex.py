import random

questions = {
  "strong": "Do ye like yer drinks strong? ",
  "salty": "Do ye like it with a salty tang? ",
  "bitter": "Are ye a lubber who likes it bitter? ",
  "sweet": "Would ye like a bit of sweetness with yer poison? ",
  "fruity": "Are ye one for a fruity finish? ",
  "spicy": "Ye like it hot, mate? "
}

ingredients = {
  "strong": ["glug of rum", "slug of whisky", "splash of gin", "shot of tequila"],
  "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon", "dash of soy sauce"],
  "bitter": ["shakes of bitters", "splash of tonic", "twist of lemon peel", "flakes of rhubarb"],
  "sweet": ["sugar cube", "spoonful of honey", "spash of cola", "stick of sugarcane"],
  "fruity": ["slice of orange", "dash of cassis", "cherry on top", "puree of mango"],
  "spicy": ["sprinkle of jalapeno", "pinch of tabasco", "drop of gunpowder", "ounce of wasabi"]
}

adjectives = ["Singing", "Dancing", "Sailing", "Drowning", "Prancing"]
nouns = ["Pirate", "Damsel", "Witch", "Mermaid", "Merman", "Land lubber"]

customers = {}

def askQuestions():
  """
  Iterate over each question contained in the questions dictionary.
  Each response will be added to an empty dictionary.
  """
  style = {}
  for key, value in questions.items():
    response = raw_input(value).lower()
    if response == "y" or response == "yes":
      style[key] = True
    else:
      style[key] = False
  return style

def constructDrink(style):
  """
  Construct a drink based on the style by the given responses.
  A random ingredient from the matched style will be selected.
  """
  drink = []
  for key, value in style.items():
    if style[key] == True:
      drink.append(random.choice(ingredients[key]))
  return drink

def newCustomer():
  """
  Iterates over main() function if there are others who needs a drink.
  If there are no more customers the shop will close and program ends.
  """
  customerNew = raw_input("Can I get anyone else a drink?")
  if customerNew == "y" or customerNew == "yes":
    main()
    print
  else:
    print "No one? Ok then on to the next step!\n\n"

def main():
  
  customerName = raw_input("\nTell me your name? ")
  customerName = customerName[0].upper() + customerName[1:].lower()
  if customerName not in customers:
    print "Alrighty then " + customerName + ", I'll fix you a drink!\n"
    customers[customerName] = {}
    customers[customerName]["drinkCount"] = 1
  elif customerName in customers:
    print "Smithereens! Another round for my mate" + customerName + "!\n"
    customers[customerName]["drinkCount"] += 1

  style = askQuestions()
  drink = constructDrink(style)
  
  print "\nYer drink is on the way!"
  print "Here ye go, a " + random.choice(adjectives) + " " + random.choice(nouns) + "'."
  print "\nAh how's the magic potion made you ask..."
  for ingredient in drink:
    print "One {}".format(ingredient)
  print ""
  
  another = raw_input("Dare you take another? ").lower()
  if another == "y" or another == "yes":
    if customers[customerName]["drinkCount"] > 2:
      print "Aye you landlubber! Enough for you!\n"
    else:
      main()
      return
  else:
    print "Goodbye then and come again my friend!\n"
    
  newCustomer()
  
   
if __name__ == '__main__':
  print "Welcome matee. Be ye landlubber or sailor this is the place for you."
  main()
