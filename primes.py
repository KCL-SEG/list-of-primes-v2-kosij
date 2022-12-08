"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError("number_of_primes must be a positive integer")

    primes_list = []
    number = 2
    while len(primes_list) < number_of_primes:
        is_prime = True
        for prime in primes_list:
            if number % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes_list.append(number)
        number += 1

    return primes_list
