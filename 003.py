
def largest_prime_factor(number):
    factor = 2
    while number > 1:
        if number % factor == 0:
            number = number // factor
        else:
            factor += 1
    return factor

number1, number2 = 13195,600851475143

assert largest_prime_factor(number1) == 29
print ("The largest prime factor for {} is {}".format(number2,largest_prime_factor(number2)) ) 