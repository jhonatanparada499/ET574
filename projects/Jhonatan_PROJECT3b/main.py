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
    indexes = range(-1,1 + 1)
    connect = 4

    for c in indexes:
      for r in indexes:
        if c == 0 and (r == -1 or r == 0): continue
        for i in range(1,connect):
          new_row = row + (r * i)
          new_column = column + (c * i)

          if new_row < 0 or new_column < 0: break 
          if new_row > (6 - 1) or new_column > (7 - 1): break
          if self.board[new_row][new_column] != player: break

        else: return True
    
    return False

if __name__ == "__main__":
  game = Connect4()
  game.play_game()
