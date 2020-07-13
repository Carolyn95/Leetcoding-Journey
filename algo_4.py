# triangle - DP problem

import pdb


class Solution:
    def minimumTotal(self, triangle):
        n = len(triangle)
        if n == 1:
            return triangle[0][0]
        for i in range(1, n):
            for j in range(len(triangle[i])):
                # pdb.set_trace()
                # print(j)
                if j == 0:
                    triangle[i][j] += triangle[i - 1][j]
                elif j == len(triangle[i]) - 1:
                    triangle[i][j] += triangle[i - 1][j - 1]
                else:
                    triangle[i][j] += min(triangle[i - 1][j],
                                          triangle[i - 1][j - 1])
        # print(min(triangle[n - 1]))
        return min(triangle[n - 1])


if __name__ == "__main__":
    s = Solution()
    triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    # triangle = [[-1], [2, 3], [1, -1, -3]]
    s.minimumTotal(triangle)
    """wrong submit
    class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        results = []
        for i in range(n):
            if len(triangle[i]) == 1:
                result = (triangle[0][0], 0)
                results.append(result)
            else:
                j = results[i - 1][1]
                min_j = triangle[i].index(
                    min(triangle[i][j], triangle[i][j + 1]))
                result = (triangle[i][min_j] + results[i - 1][0], min_j)
                results.append(result)
        return results[n - 1][0]
    """
