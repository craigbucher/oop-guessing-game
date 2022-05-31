import random

class GuessingGame():
    def __init__(self, answer):
        self.answer = answer
        #self.user_guess = user_guess
        self.correct = False
    
    def guess(self, user_guess):
      if last_guess > self.answer:
        return 'high'
      elif last_guess < self.answer:
        return 'low'
      else:
        return True

    def solved(self):
      if last_result =='correct':
        return True
      else:
        return False

# ----- DRIVER CODE -----
game = GuessingGame(random.randint(1,10))
last_guess  = None
last_result = None

while game.solved() == False:
  if last_guess != None: 
    print(f"Oops! Your last guess ({last_guess}) was {last_result}.")
    print("")

  last_guess  = int(input("Enter your guess: "))
  last_result = game.guess(last_guess)


print(f"{last_guess} was correct!")