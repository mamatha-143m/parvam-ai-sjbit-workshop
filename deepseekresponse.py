def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def print_primes(limit):
    """Print all prime numbers up to a given limit."""
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    
    print(f"Prime numbers up to {limit}:")
    print(primes)
    return primes

# Example usage
if __name__ == "__main__":
    try:
        limit = int(input("Enter the upper limit: "))
        print_primes(limit)
    except ValueError:
        print("Please enter a valid integer.")
