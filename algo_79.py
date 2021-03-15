# word search
# Given an m x n gird of characters board and a string word, return true if word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.


class Solution:

  def exist(self, board, word):  #  -> bool
    print()
    # [[(0, 0), (0, 1), (0, 2), (0, 3)],
    #  [(1, 0), (1, 1), (1, 2), (1, 3)],
    #  [(2, 0), (2, 1), (2, 2), (2, 3)]]


if __name__ == '__main__':
  board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
  word = "ABCCED"
  # OUTPUT = true
  sol = Solution()
  sol.exist(board, word)