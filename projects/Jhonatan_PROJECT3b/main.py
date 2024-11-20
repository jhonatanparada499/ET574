# Connect 4 Game
class Connect4:
  def __init__(self):
    self.board = [[' ' for _ in range(7)] for _ in range(6)]
    self.current_player = 'X'

    # New object attributes created
    # Desc: coordinates needed in the check_win method
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
        # self.check_win(self.current_player, self.board.index(row), column)

        # sets the indexes of current's player chip        
        self.current_row = self.board.index(row)
        self.current_column = column

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
    
  def check_win(self, player):
    # Uses the coordinates of the current's player chip as starting point
    row = self.current_row
    column = self.current_column
    
    # define the physical dimensions of the board
    rows = len(self.board)
    cols = len(self.board[0])
    connect = 4
    #cols, rows, connect = 7, 6, 4
    
    # Is there space to insert 4 chips to the left? the right? up? down?
    l, r, u, d = None, None, None, None

    # Allowed winning combinations
    connections = {
      'l': False,
      'r': False,
      'd': False,
      'l_u': False,
      'l_d': False,
      'r_u': False,
      'r_d': False
    }

    # There are 8 independent if statements

    # Check left possibility to win
    if column >= (connect - 1):
      # print('user might win left')
      l = True
      i = 1
      while i != connect:
        if self.board[row][column - i] == player: i += 1; continue # [row][column - i]
        # print('user did not win left'); break
        break
      else: connections['l'] = True

    # Check right possibility to win
    if (cols - 1) - column >= (connect - 1):
      # print('user might win right')
      r = True
      i = 1
      while i != connect:
        if self.board[row][column + i] == player: i += 1; continue # [row][column + i]
        # print('user did not win right'); break
        break
      else: connections['r'] = True

    # Check up possibility to win
    if row >= (connect - 1):
      u = True
      # print('user might win up')

    # Check down possibility to win
    if (rows - 1) - row >= (connect - 1):
      # print('user might win down')
      d = True
      i = 1
      while i != connect:
        if self.board[row + i][column] == player: i += 1; continue # [row + i][column - i]
        # print('user did not win down'); break
        break
      else: connections['d'] = True

    if l and u:
      # print('user might win diagonal left-up')
      i = 1
      while i != connect:
        if self.board[row - i][column - i] == player: i += 1; continue # [row - i][column - i]
        # print('user did not win diagonal left-up'); break
        break
      else: connections['l_u'] = True
    if l and d:
      # print('user might win diagonal left-down')
      i = 1
      while i != connect:
        if self.board[row + i][column - i] == player: i += 1; continue # [row + i][column - i]
        # print('user did not win diagonal left-down'); break
        break
      else: connections['l_d'] = True
    if r and u:
      # print('user might win diagonal right-up')
      i = 1
      while i != connect:
        if self.board[row - i][column + i] == player: i += 1; continue # [row - i][column + i]
        # print('user did not win right-up'); break
        break
      else: connections['r_u'] = True
    if r and d:
      # print('user might win diagonal right-down')
      i = 1
      while i != connect:
        if self.board[row + i][column + i] == player: i += 1; continue # [row + i][column + i]
        # print('user did not win right-down'); break
        break
      else: connections['r_d'] = True

    # this dictionary contains all the winning combinations a player may have
    # because by placing a chip, sometimes more than one connection can be created
    wins = [k for k,v in connections.items() if v==True]

    if wins: return True
    return False

if __name__ == "__main__":
  game = Connect4()
  game.play_game()

