def get_prime_factors(num):
    divisor = 2
    factors = list()
    while (divisor <= num):
        if (num % divisor) == 0:
            factors.append(divisor)
            num = num / divisor
        else:
            divisor += 1
    return factors