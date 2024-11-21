# Connect 4 Game
class Connect4:
  def __init__(self):
    self.board = [[' ' for _ in range(7)] for _ in range(6)]
    self.current_player = 'X'
    self.current_row = None
    self.current_column = None

  def switch_player(self):
    self.current_player = 'O' if self.current_player == 'X' else 'X'

  def print_board(self):
    for row in self.board:
      print('|', end='')
      for cell in row:
        print(cell, end='|')
      print()
    print('---------------')
    print(' 1 2 3 4 5 6 7')

  def drop_chip(self, column):
    if not 1 <= column <= 7: return False
    column -= 1

    # checks that the column is not full so it does not waste time
    if self.board[0][column] != ' ': return False

    for row in reversed(self.board):
      if row[column] == ' ':
        row[column] = self.current_player

        # sets the coordinates of current's player chip
        self.set_coordinates(self.board.index(row), column)

        break
        
    return True
  
  def play_game(self):
    game_over = False
    while not game_over:
      self.print_board()
      print(f"Player {self.current_player}'s turn.")

      try:
        column = int(input("Enter the column number (1-7): "))
      except ValueError:
        print("Invalid input. Please enter a valid column number.")
        continue

      if not self.drop_chip(column):
        print("Column is full or out of range. Try again.")
        continue

      if self.check_win(self.current_player):
        self.print_board()
        print(f"Player {self.current_player} wins!")
        game_over = True
      
      self.switch_player()

  def set_coordinates(self, row, column):
    self.current_row = row
    self.current_column = column

  def get_coordinates(self):
    return self.current_row, self.current_column

  def check_win(self, player):
    row, column = self.get_coordinates()
    connect = 4

    i = -1 # i represents the the column
    while i != (1 + 1): # range (-1, 0, 1) for column
      
      y = -1 # y represents the row
      while y != (1 + 1): # range (-1, 0, 1) for row
        
        # skips self and upward cell
        if i == 0 and (y == -1 or y == 0): y += 1; continue

        x = 1 # x represents the number of chips that need to be aligned to win the game
        while x != (connect):
          
          # Defines the coordinates of a cell after a transition from the current chip
          new_row = row + (y * x)
          new_column = column + (i * x)
          
          # If either coordinate is negative, that means that the coordinate is out of range
          if new_row < 0 or new_column < 0: break

          # checks that the target cell exists and that it is equal to player
          try:
            if self.board[new_row][new_column] != player: break
          except: break

          x += 1
        else: 
          # getting to this point means that everything went good during the loop
          # therefore, there a specified number of chips are aligned
          return True 

        y += 1  
      i += 1
    return False

if __name__ == "__main__":
  game = Connect4()
  game.play_game()
