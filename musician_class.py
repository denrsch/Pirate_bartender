#diana = Musician(["Twang", "Thrumb", "Bling"])
#nora = Musician(["Boink", "Bow", "Boom"])
#diana and nora are both musicians

import pdb
pdb.set_trace()

class Musician(object):
  def __init__(self, sounds):
      self.sounds = sounds

  def solo(self, length):
    for i in range(length):
      print self.sounds[i % len(self.sounds)],
      print ""

class Bassist(Musician):
  def __init__(self):
    super(Bassist, self).__init__(["Twang", "Thrumb", "Bling"])
      
class Guitarist(Musician):
  def __init__(self):
    super(Guitarist, self).__init__(["Boink", "Bow", "Boom"])
    
if __name__ == "__main__":
  diana = Musician(["Twang", "Thrumb", "Bling"])
  diana.solo(3)
      
      