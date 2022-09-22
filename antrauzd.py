# Spausdinti pirminių skaičių progresiją iki 2**16
primes = [2, 3]
for number in range(4, 2**16):
    for primal in primes:
        if number % primal == 0:
            break
    else:
        primes.append(number)
print(primes)