import random
import string

class BoggleBoard:
    
  list1 = ["____"]
  list2 = ["____"]
  list3 = ["____"]
  list4 = ["____"]
  
  boggle_dice = {
      'die1': ['A', 'A', 'E', 'E', 'G', 'N'], 
      'die2': ['E', 'L', 'R', 'T', 'T', 'Y'], 
      'die3': ['A', 'O', 'O', 'T', 'T', 'W'], 
      'die4': ['A', 'B', 'B', 'J', 'O', 'O'], 
      'die5': ['E', 'H', 'R', 'T', 'V', 'W'], 
      'die6': ['C', 'I', 'M', 'O', 'T', 'U'], 
      'die7': ['D', 'I', 'S', 'T', 'T', 'Y'], 
      'die8': ['E', 'I', 'O', 'S', 'S', 'T'], 
      'die9': ['D', 'E', 'L', 'R', 'V', 'Y'], 
      'die10': ['A', 'C', 'H', 'O', 'P', 'S'], 
      'die11': ['H', 'I', 'M', 'N', 'Q', 'U'], 
      'die12': ['E', 'E', 'I', 'N', 'S', 'U'], 
      'die13': ['E', 'E', 'G', 'H', 'N', 'W'], 
      'die14': ['A', 'F', 'F', 'K', 'P', 'S'], 
      'die15': ['H', 'L', 'N', 'N', 'R', 'Z'], 
      'die16': ['D', 'E', 'I', 'L', 'R', 'X']
  }
    
  def __init__(self):
    print(BoggleBoard.list1[0])
    print(BoggleBoard.list2[0])
    print(BoggleBoard.list3[0])
    print(BoggleBoard.list4[0])

  def shake(self):
    string1 = ""
    string2 = ""
    string3 = ""
    string4 = ""
    
    for key, value in enumerate(BoggleBoard.boggle_dice.values()):
      random_number = random.randint(0, 5)
      if key < 4:
        string1 += value[random_number]
      elif 4 <= key < 8:
        string2 += value[random_number]
      elif 8 <= key < 12:
        string3 += value[random_number]
      elif 12 <= key < 16:
        string4 += value[random_number]
        
    print(string1)
    print(string2)
    print(string3)
    print(string4)
      
      

test = BoggleBoard()
test.shake()