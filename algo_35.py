# 224 count primes
class Solution:
    def countPrimes(self, n: int) -> int:
        count = 1
        for i in range(3,n):
            if self.isPrimes(i):
                count += 1
        return count
    def isPrimes(self, num: int) -> bool:
        for i in range(2, int(sqrt(num))+1):
            if num%i == 0:
                return False
        return False
