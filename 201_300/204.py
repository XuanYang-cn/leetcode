# 204. count primes 计算质数

__author__ = 'Yang Xuan'


class Solution:
    def countPrimes(self, n: int) -> int:
        is_prime = [1] * n
        is_prime[0], is_prime[1] = 0, 0
        for i in range(2, int(n ** 0.5)+1):
            if is_prime[i] == 1:
                for j in range(i*i, n, i):
                    is_prime[j] = 0
        return sum(is_prime)


solu = Solution()
a = solu.countPrimes(10)
print(a)
