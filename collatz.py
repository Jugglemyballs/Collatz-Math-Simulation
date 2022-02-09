if __name__ == '__main__':
  
  def collatz_squance(x):
    seq = [x]
    
    if x < 1:
      return []
    
    
    while x > 1:
      if x % 2 == 0:
        x = x / 2
        
      elif x % 2 == 1:
        x = x * 3 - 1
      
      x = int(x)
      
      seq.append(x)
      
    return seq
  
while True:
  number = input("Enter a positive integer: ")
  
  try:
     val = int(number)
      if val < 0:
        print("Sorry, input must be a positive integer, try again")
        continue
      break
    except ValueError:
      print("That's not an integer!")
      
    number = val
    
    z = collatz_sequence(number)
    
    print(z)
    
    print('Ending Number: ' + str(z[-1]))
    
    print('Length: ' + str(len(z)))
    
    
