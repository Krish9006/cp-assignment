def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_alternate_primes(N):
    prime_count = 0
    num = 2
    alternate_primes = []
    for _ in range(N):
        while True:
            if is_prime(num):
                alternate_primes.append(num)
                num += 1
                prime_count += 1
                break
            num += 1
    return alternate_primes[::2]

# Example Input
N = 5
print(" ".join(str(prime) for prime in generate_alternate_primes(N)))
