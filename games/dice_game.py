class DiceGame:
  def __init__(self):
    self.start_new_game()

  def start_new_game(self):
    self.turn = 1
    self.point = None
    self.finished = False
    self.result = ""

  def validate_roll(self, roll):
    try:
      roll = int(roll)
    except ValueError:
      return False, "Roll must be a number"

    if roll <2 or roll > 12:
      return False, "Roll must be between 2 and 12"

    return True, roll

  def play_turn(self, roll):
    if self.finished:
      return self.result
    
    valid, value = self.validate_roll(roll)
    if not valid:
      return value
    
    roll = value

    if self.turn == 1:
      if roll in [2, 3, 12]:
        self.result = f"Turn 1: Rolled {roll}. You lose"
        self.finished = True

      elif roll in [7, 11]:
        self.result = f"Turn 1: Rolled {roll}. You win"
        self.finished = True

      else:
        self.point = roll
        self.result = f"Turn 1: Rolled {roll}. Point is {self.point}"
        self.turn += 1

    else:
      if roll == 7:
        self.result = f"Turn {self.turn}: Rolled 7. You lose"
        self.finished = True

      elif roll == self.point:
        self.result = f"Turn {self.turn}: Rolled {roll}. You win"
        self.finished = True

      else:
        self.result = f"Turn {self.turn}: Rolled {roll}. Keep rolling, no results yet"
        self.turn += 1
    
    return self.result