import random

questions = {
    "fruity": "are ye a fruity drink lubber?",
    "smokey": "Or Do ye prefer something smokey, like mezcal or whisky?",
    "salty": "would ye like something salty like the sea?",
    "citrus": "would ye like a lime in that?"
}

ingredients = {
    "fruity": ["splash of orange juice"], 
    "smokey": ["shot of mezcal", "shot of whiskey"],
    "salty": ["cup of lemonade", "glug of lime juice", "salt around the rim"],
    "citrus": ["lemon juice", "grapefruit juice", "cranberry juice", "two shots of vodka", "slice of lime"],
   
}

fruity = raw_input(questions['fruity'] + ' ').lower().strip() in ['y', 'yes']
smokey = raw_input(questions['smokey'] + ' ').lower().strip() in ['y', 'yes']
salty = raw_input(questions['salty'] + ' ').lower().strip() in ['y', 'yes']
citrus = raw_input(questions['citrus'] + ' ').lower().strip() in ['y', 'yes']

print "So, %r fruity, %r smokey, %r salty and %r citrus? Is that correct?" % (fruity, smokey, salty, citrus)

def customer_drink_order():
  drink_ingredients = [] 
  if fruity == True:
    drink_ingredients.append(ingredients['fruity'][0])
  else:
    print "ok, we'll skip fruity."
    
  if smokey == True:
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

