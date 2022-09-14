class MyNumber:
    def __init__(self, value):
        self.value = value

    def find_prime_dividers(self):
        n = self.value
        prime_dividers = []
        while n > 1:
            for i in range(2, n + 1):
                if n % i == 0:
                    prime_dividers.append(i)
                    n = int(n / i)
                    break
        self.prime_dividers = prime_dividers
        return prime_dividers

    def find_max_prime_divider(self):
        return max(self.find_prime_dividers())

n1 = MyNumber(600851475143)
print(n1.find_max_prime_divider())
