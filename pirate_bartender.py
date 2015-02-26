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

print "hello! Welcome to me Bar! My name is Captain Blackbeard, and I will be your server!"
name = raw_input("What is yer name? ")
print "Welcome %r! We are glad to have ye today. Let's see what I can get ye." % (name)

fruity = raw_input(questions['fruity'] + ' ').lower().strip() in ['y', 'yes']
smokey = raw_input(questions['smokey'] + ' ').lower().strip() in ['y', 'yes']
salty = raw_input(questions['salty'] + ' ').lower().strip() in ['y', 'yes']
citrus = raw_input(questions['citrus'] + ' ').lower().strip() in ['y', 'yes']

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
  drink_names = [] 
  if fruity == True & smokey == True:
    drink_names.append(random.choice(drink_names['fruity']))
  for drink_name in drink_names:
    print drink_name
       
  if smokey == True:
    drink_names.append(ingredients['smokey'][0])
  print "ok, we'll skip smokey."
    
  if fruity == True & salty == True:
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

    
    


