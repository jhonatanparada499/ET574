# Connect 4 Game

class Connect4:
  def __init__(self):
    self.board = [[' ' for _ in range(7)] for _ in range(6)]
    self.current_player = 'X'

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
    """
    Drops a chip into the selected column of the Connect 4 board.

    Args:
      column (int): The column number where the chip is to be dropped. It must be between 1 and 7.

    Returns:
      bool: True if the chip was successfully dropped, False if the column is full or if the column is out of range.
    """
    # TO BE IMPLEMENTED: Check if the column is out of range. The valid column # is from 1 to 7. 
    if not 1 <= column <= 7: return False


    # TO BE IMPLEMENTED: Use a while-loop to check row by row for an empty cell on the column. 
    # Hint: start with the highest row number and decrement the row number each time in the loop.


    # row = len(self.board)
    # while row > 0:
    #   row -= 1
    #   if self.board[row][column - 1] == ' ':
    #     self.board[row][column - 1] = self.current_player
    #     self.print_board()
    #     break
    # else: return False

    # TO BE IMPLEMENTED:  If the column is full, return False. Question: what indicates the column is full?
    # ANSWER: If the while loop gets to its else portion, that would mean that it was not broken by
    # a break statement, which means it finished the loop and it did not find any empy slot. Therefore,
    # that returns false.

    # TO BE IMPLEMENTED:  Drop the current player's chip into the selected slot. This simply means mark the cell 
    # you found above to self.current_player, which is either X or O

    for row in reversed(self.board):
      if row[column - 1] == ' ':
        row[column - 1] = self.current_player
        self.print_board()
        break
    else: return False
    
    
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
      
      self.switch_player()

if __name__ == "__main__":
  game = Connect4()
  game.play_game()
