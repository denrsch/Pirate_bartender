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

fruity = raw_input('are ye a fruity drink lubber?')
smokey = raw_input('Or Do ye prefer something smokey, like mezcal or whisky?')
salty = raw_input('would ye like something salty like the sea?')
citrus = raw_input('would ye like a lime in that?')

print "So, %r fruity, %r smokey, %r salty and %r citrus? Is that correct?" % (fruity, smokey, salty, citrus)

def customer_drink_order():
  for True in fruity:
    print "we'll add a splash of orange juice"
  else:
    print "ok, we'll skip that."
    
  elif smokey == True:
    print "I'll add a shot of mezcal and shot of whiskey."
  else:
    print "ok, we'll skip that."
    
  elif salty == True:
    print "I'll add some lemonade and put salt around the rim."
  else:
    print "ok, we'll skip that."
    
  elif citrus == True:
    print "I'll throw in a slice of lime."
  else:
    print "ok, we'll skip that."


