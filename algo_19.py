# 7 reverse integer
class Solution:
    def reverse(self, x: int) -> int:
        str_x = list(str(x))
        opt = str_x.pop(0) if str_x[0] in ['+', '-'] else None
        print(str_x)
        new_x = 0
        for i in range(len(str_x)):
            new_x += int(str_x[i]) * 10 ** i
        print(new_x)
        if opt == '-':
            return -new_x
        return new_x


if __name__ == '__main__':
    s = Solution()
    x = -123
    s.reverse(x)

