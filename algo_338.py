# leetcode 338 counting bits
import pdb


class Solution1:

  def countBits(self, num):
    """
        0=>[0] => [0]
        1=>[0, 1] => [0, 1]
        2=>[0, 1, 2] => [0, 1, 10]
        3=>[0, 1, 2, 3] => [0, 1, 10, 11]
        4=>[0, 1, 2, 3, 4] => [0, 1, 10, 11, 100]
        5=>[0, 1, 2, 3, 4, 5] => [0, 1, 10, 11, 100, 101]
        6=>[0, 1, 2, 3, 4, 5, 6] => [0, 1, 10, 11, 100, 101, 110]
        """
    res = []
    for i in range(num + 1):
      res.append(self.count(i))
    return res

  def count(self, num):
    if num == 0:
      return 0
    if num % 2 == 1:
      return self.count(num - 1) + 1
    return self.count(num // 2)


class Solution2:

  def countBits(self, num):
    return [bin(i).count('1') for i in range(num + 1)]


class OptimizedSolution1:

  def countBits(self, num):
    self.bit_count = [0] * (num + 1)
    return [self.count(i) for i in range(num + 1)]

  def count(self, num):
    if num == 0:
      return 0
    if self.bit_count[num] != 0:
      return self.bit_count[num]
    if num % 2 == 1:
      res = self.count(num - 1) + 1
    else:
      res = self.count(num // 2)
    self.bit_count[num] = res
    return res


if __name__ == '__main__':
  test = 1
  sol = OptimizedSolution1()
  res = sol.countBits(test)
  print(res)
