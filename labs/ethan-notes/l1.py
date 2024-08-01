'''
Author: Ethan Gilles
Date: 7/29/24
Class: COS280 - Discrete Math
Assignment: Lab 1
'''
import math

'''
Learning Objectives:
1. Comments (single-line/block) - 0 questions
2. Assignments and Variables - 2 questions
3. Math operations - 4 questions
4. Logical and relational operators - 3 questions
5. if-then-else - 4 questions
6. Loops - 5 questions
7. Lists - 4 questions
8. Random Numbers - 0 questions
9. Functions - 4 questions

Notes:
Random numbers were not addressed in the questions. 
Calculating large primes takes a long time and in some cases wasn't loading at
all for larger primes.
Question 4's wording was hard to understand.
'''


'''
Question 1: 
Write a functions that determins if a number is prime

LO's:
- Math operations
- Logical and relational operators
- if-then-else
- Loops
- Functions
'''

def isPrime(n):
    if n==2 or n==3: return True
    if n % 2==0 or n < 2: return False
    for i in range(3, int(n**0.5)+1, 2):   # only odd numbers
        if n%i==0:
            return False    
    return True

# print(isPrime(617))

'''
Question 2:
Write a function that lists all primes less than or equal a given positive 
integer

LO's:
- if-then-else
- Lists
- Loops
- Functions
'''

def listPrimes(x):
    y = []
    for i in range(1, x+1):
        if(isPrime(i)):
            y.append(i)
    return y

# print(listPrimes(617))

'''
Question 3:
Use a loop and the function above to determine whether  2^p - 1 is prime,
for each of the primes not exceeding 100.

LO's:
- Lists 
- Loops 
- Functions
NOTE : had extreme runtimes for p > 59 on my personal laptop.
'''

# for x in listPrimes(100):
#     print("p={:d}  2^p-1= {:d} prime?={:b}".format(x, 2**x-1, isPrime(2**x-1)))

'''
Question 4:
Show that n^2+n+41 is prime for all integers n with 0≤n≤39, but is not prime
when n=40. Is there a polymomial in 'n' with integer coefficients and degree 
greater than zero that always takes on a prime value when n is a positive 
integer?

NOTE: Not sure what the second part of the question is asking? Should I be
testing different coefficients with the current polynomial
(eg. 2n^2 + 2n + 41, 3n^2 + 3n + 41, etc.)?

LO's:
- Math operations
'''

# for x in range(41):
#     print("n={:d} prime?={:b}".format(x, isPrime(x**2 + x + 41)))


'''
Question 5: 
Find 10 different primes each with 100 digits.

NOTE: Again, was having pretty extreme runtimes and couldn't actually get a 
list to output but here is the code I would use

LO's:
- Assignments and Variables
- Math operations
- Logical and relational operators
- if-then-else
- Loops
- Lists 
- Functions 
'''

def listBigPrimes():
    primes = listPrimes(617)
    bigPrimes = []
    for i in primes:
        if i > 331:     # 2**331 - 1 has 100 digits.
            n = 2**i - 1
            if isPrime(n):
                bigPrimes.append(n)
        if(len(bigPrimes) >= 10):
            return bigPrimes


'''
Question 6: 
Find all pseudoprimes to the base 2, that is, composite integers n 
such that 2^n−1≡1(mod n), where n does not exceed 10000.

LO's:
- Assignments and Variables 
- Math operations 
- Logical and relational operators
- if-then-else
- Loops
- Lists
- Functions
'''

def listPseudoPrimes(x):
    pseudoPrimes = []
    for n in range(1, x):
        if not isPrime(n) and (2**n - 1) % n == 1:
            pseudoPrimes.append(n)
    return pseudoPrimes

# print(listPseudoPrimes(10000))
