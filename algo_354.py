# Russian doll envelopes
# Input: [[5, 4], [6, 4], [6, 7], [2, 3]]
# Output: 3
# Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
# res = []
#


class Solution:

  def maxEnvelopes(self, envelopes):
    envelopes.sort()
    print(envelopes)
    count = 0
    for cur, envelope in enumerate(envelopes):
      cur_i, cur_j = envelope[0], envelope[1]
      for nxt in envelopes[cur + 1:]:
        nxt_i, nxt_j = nxt[0], nxt[1]
        if cur_i < nxt_i and cur_j < nxt_j:
          count += 1
    return count


if __name__ == '__main__':
  envelopes = [[5, 4], [6, 4], [6, 7], [2, 3]]
  sol = Solution()
  res = sol.maxEnvelopes(envelopes)
  print(res)