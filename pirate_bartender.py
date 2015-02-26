import random

questions = {
    "fruity": "are ye a fruity drink lubber?",
    "smokey": "Or Do ye prefer something smokey, like mezcal or whisky?",
    "salty": "would ye like something salty like the sea?",
    "citrus": "would ye like a lime in that?"
}

ingredients = {
    "fruity": ["splash of orange juice"], 
    "smokey": ["shot of mezcal"],
    "salty": ["glug of lime juice", "salt around the rim"],
    "citrus": ["lemon juice", "grapefruit juice", "cranberry juice", "two shots of vodka", "slice of lime"],
   
}

drink_names = {
  "fruity": ["smokey sunrise", "bright and stormy"],
  "smokey": ["smoke signals", "Start Yer Engines"],
  "salty": ["Song of the Sea"],
  "citrus": ["life in the tropics", "The Anti-Scurvy"]
  
}

preferences = {}

while True:
  print "hello! Welcome to me Bar! My name is Captain Blackbeard, and I will be your server!"
  name = raw_input("What is yer name? ")
  print "Welcome %s! We are glad to have ye today. Let's see what I can get ye." % (name)
  if 1: # preferences.has_key...: # Complete
    fruity = raw_input(questions['fruity'] + ' ').lower().strip() in ['y', 'yes']
    smokey = raw_input(questions['smokey'] + ' ').lower().strip() in ['y', 'yes']
    salty = raw_input(questions['salty'] + ' ').lower().strip() in ['y', 'yes']
    citrus = raw_input(questions['citrus'] + ' ').lower().strip() in ['y', 'yes']
  else:
    print "I'm lazy, making what you had before..."
    ## Final exercise: Here, ask whether they want the same drink as last time.  If not, ask them the four questions again.
    fruity = preferences[name]['fruity']
    smokey = None ## ... Complete this 
  preferences[name] = {'fruity': fruity, 'smokey': smokey, 'salty': salty, 'citrus': citrus}
  print preferences
 
  
  print "So, %r fruity, %r smokey, %r salty and %r citrus? Is that correct?" % (fruity, smokey, salty, citrus)
  
  def customer_drink_order():
    drink_ingredients = []
    
    if fruity == True:
      drink_ingredients.append(drink_names['fruity'][0])
    else:
      print "ok, we'll skip fruity."
      
    if fruity == True:
      drink_ingredients.append(ingredients['smokey'][0])
    else:
      print "ok, we'll skip smokey."
      
    if salty == True:
      drink_ingredients.append(random.choice(ingredients['salty']))
    else:
      print "ok, we'll skip salty."
      
    if citrus == True:
      drink_ingredients.append(random.choice(ingredients['citrus']))
    else:
      print "ok, we'll skip citrus."
    print "Drink ingredients are "
    for ingredient in drink_ingredients:
      print ingredient 
  
      
  customer_drink_order() 
  
  def customer_drink_name():
    drink_name = []   
    if fruity == True:
      drink_name.append(random.choice(drink_names['fruity']))
    if smokey == True:
      drink_name.append(random.choice(drink_names['smokey']))
    if salty == True:
      drink_name.append(random.choice(drink_names['salty']))
    if citrus == True:
      drink_name.append(random.choice(drink_names['citrus']))
    return drink_name
  
  #print customer_drink_name()
  
  print "Here's your drink, %s! It's called '%s' " %  (name, ' '.join(customer_drink_name()))
