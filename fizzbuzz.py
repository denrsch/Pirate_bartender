#import pdb
#pdb.set_trace()

upperbound = raw_input("how high should we go?")

for n in range(0,int(upperbound)):
  if (n % 5 == 0) and (n % 3 == 0):
    print "fizzbuzz"
  
  elif n % 3 == 0:
    print "fizz"
  
  elif n % 5 == 0:
    print "buzz"
  
  else:
    print(n)