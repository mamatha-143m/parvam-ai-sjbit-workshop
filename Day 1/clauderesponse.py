def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def get_primes_up_to(limit):
    """Return a list of all prime numbers up to a given limit."""
    return [n for n in range(2, limit + 1) if is_prime(n)]


def get_first_n_primes(n):
    """Return the first n prime numbers."""
    primes = []
    candidate = 2
    while len(primes) < n:
        if is_prime(candidate):
            primes.append(candidate)
        candidate += 1
    return primes


def print_primes(primes):
    """Print a list of prime numbers nicely."""
    print(f"Found {len(primes)} prime(s): {primes}")


# --- Example usage ---

# 1. Primes up to 50
print("Primes up to 50:")
print_primes(get_primes_up_to(50))

# 2. First 10 primes
print("\nFirst 10 primes:")
print_primes(get_first_n_primes(10))

# 3. Check individual numbers
print("\nIs 17 prime?", is_prime(17))
print("Is 18 prime?", is_prime(18))