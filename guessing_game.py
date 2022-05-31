import random

class GuessingGame():
    def __init__(self, answer, last_guess, last_result):
        self.answer = answer
        self.last_guess = last_guess
        self.last_result = last_result
    
    def guess(self):
      if self.last_guess > self.answer:
        return 'high'
      elif self.last_guess < self.answer:
        return 'low'
      else:
        return 'correct'

    def solved(self):
      if self.last_result =='correct':
        return True
      else:
        return False

# ----- DRIVER CODE -----
game = GuessingGame(random.randint(1,10), None, None)
# last_guess  = None
# last_result = None

while game.solved() == False:
  if game.last_guess != None: 
    print(f"Oops! Your last guess \"({game.last_guess})\" was {game.last_result}.")
    print("")

  game.last_guess  = int(input("Enter your guess: "))
  game.last_result = game.guess()


print(f"{game.last_guess} was correct!")