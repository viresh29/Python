from math import sqrt
Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = [((float(9)/5)*x + 32) for x in Celsius]

print(Fahrenheit)

# The following list comprehension creates the Pythagoreon triples.

list_1 = [(x, y, z) for x in range(1, 30) for y in range(x, 30)
          for z in range(y, 30) if x**2 + y**2 == z**2]

print(list_1)

# Cross product of two sets

colors = ['red', 'green', 'yellow', 'blue']
things = ['house', 'car', 'tree']

colored_things = [(x, y) for x in colors for y in things]

print(colored_things)

# Generator comprehension

x = (x ** 2 for x in range(20))
print(x)

x = list(x)
print(x)

# Primes and nonprimes

noprimes = [j for i in range(2, 8) for j in range(i*2, 100, i)]
primes = [x for x in range(2, 100) if x not in noprimes]
print(primes)


n = 100
sqrt_n = int(sqrt(n))
no_primes = [j for i in range(2, sqrt_n) for j in range(i*2, n, i)]

print(no_primes)


for p in range(2, n+1):
    for i in range(2, p):
        if p % i == 0:
            break
    else:
        print(p)
print('Done')
