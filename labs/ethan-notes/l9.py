'''
Author: Ethan Gilles
Date: 8/1/24
Class: COS280 - Discrete Math
Assignment: Lab 9
'''
import math
import random

'''
Learning Objectives:
1. Test and verify subset relations. - 3 questions
2. Test and verify set identities. - 7 questions
3. Write, test, and verify DeMorgan's laws. - 1 questions

Notes:
- 2 questions without LO's (9 & 10)
- Question 10 needed 3 packages using pip. Definitely worth noting them.
- pip install matplotlib matplotlib_venn PyQt6
'''

def randset(M):
    list1 = range(1,M)
    n = random.choice(list1)
    S = set(list1)
    for i in range(n):
        x = random.choice(sorted(S))
        S = S - {x}
    return S

A = {1,2,3}
B = {3,1,2}
C = {3,1,2,4,6,5}
D = {2,5}

'''
Question 1:
Given any two sets, A and B, write a function issubset that 
determines whether A ⊆ B.

LO's:
- Test and verify subset relations 
- Test and verify set identities
''' 
 
# for A ⊆ B
def issubset(A,B):
    for item in A:
        if not item in B:
            return False
    return True

# print(f"A ⊆ B - {issubset(A,B)}")
# print(f"C ⊆ D - {issubset(C,D)}")

'''
Question 2:
Write a function that returns A^c given that A is a subset of the universal set U.

LO's:
- Test and verify set identities
'''

U = set(range(1,100))
def complement(A):
    B = set()
    for item in U:
        if not item in A:
            B.add(item)
    return B

# print(f"Complement of A is {complement(A)}")


'''
Question 3:
Verify for any two sets, A ∩ B ⊆ A and A ∩ B ⊆ B.

LO's:
- Test and verify subset relations 
- Test and verify set identities
'''

A = randset(50)
B = randset(50)
# print(f"A ∩ B ⊆ A = {issubset(A & B, A)}")
# print(f"A ∩ B ⊆ B = {issubset(A & B, B)}")


'''
Question 4:
Verify for any two sets, A ⊆ A ∪ B and B ⊆ A ∪ B.

LO's:
- Test and verify subset relations 
- Test and verify set identities
'''

# print(f"A ⊆ A ∪ B = {issubset(A, A | B)}")
# print(f"B ⊆ A ∪ B = {issubset(B, A | B)}")


'''
Question 5:
Use randset() to generate three sets, then verify the transitive property of subsets.
A ⊆ B ∧ B ⊆ C ⇒ A ⊆ C

LO's:
- Test and verify set identities
'''

while not (A <= B and B <= C):
    A = randset(50)
    B = randset(50)
    C = randset(50)
# print(f"A ⊆ B ∧ B ⊆ C ⇒ A ⊆ C = {issubset(A,C)}")


'''
Question 6:
Verify the following set identities: Associative, Distributive, Double Complement,
Idempotent, Set Difference, Absorption.

LO's:
- Test and verify set identities
'''

A = randset(50)
B = randset(50)
C = randset(50)

printLaws = False
if printLaws:
    # A∩B=B∩A and A∪B=B∪A.
    print(f"Communtative: {(A & B == B & A) and (A | B == B | A)}")

    # A∪(B∪C)=(A∪B)∪C
    print(f"Associative union: {(A | (B | C) == (A | B) | C)}")
    # A∩(B∩C)=(A∩B)∩C
    print(f"Associative intersection: {(A & (B & C) == (A & B) & C)}")

    # A∪(B∩C)=(A∪B)∩(A∪C)
    print(f"Distributive union: {( (A | (B & C)) == ((A | B) & (A | C)) )}")
    # A∩(B∪C)=(A∩B)∪(A∩C)
    print(f"Distributive intersection: {( (A & (B | C)) == ((A & B) | (A & C)) )}")

    # (A^c)^c=A
    print(f"Double complement: {complement(complement(A)) == A}")

    # A∪A=A and A∩A=A
    print(f"Idempotent laws: {(A | A == A) and (A & A == A)}")

    # A−B=A∩Bc
    print(f"Set difference: {A - B == A & complement(B)}")

    # A∪(A∪B)=A and A∩(A∪B)=A
    print(f"Absorption laws: {(A | (A & B) == A) and (A & (A | B) == A)}")


'''
Question 7:
Similar to above, verify DeMorgan's Laws

LO's:
- Write, test, and verify DeMorgan's laws.
'''

# (A∪B)c=Ac∩Bc
# print(f"DeMorgan's Law Union: {complement(A | B) == complement(A) & complement(B)}")
# (A∩B)c=Ac∪Bc
# print(f"DeMorgan's Law Intersection: {complement(A & B) == complement(A) | complement(B)}")


'''
Question 8:
Use len() to determine the cardinality of a set. Then determine the number of 
subsets of a randomly generated set.

LO's 
- Test and verify set identities
'''

# print(f"Cardinality - {len(A)}")
# print(f"Number of subsets - {2 ** len(A)}")


'''
Question 9:
Write a set comprehension that contains the set of 
tuples (x,y) for x∈{1,2,3} and y∈{2,5}


LO's:
- none
'''
X = {1,2,3}
Y = {2,5}

def comprehension(X,Y):
    tuples = set()
    for x in X:
        for y in Y:
            tuples.add( (x,y) )
    return tuples

# print(comprehension(X,Y))


'''
Question 10:
Test it with several randomly generated sets A and B. Does it work for three sets?

LO's:
- none

Notes:
- I couldn't get it to work for 3 sets.
- 3 pip commands, definitely worth noting for any students not familiar with packages in Python.
pip install matplotlib
pip install matplotlib_venn 
pip install PyQt6
'''

import matplotlib.pyplot as plt
from matplotlib_venn import venn2

# Create sets for the two circles
A = randset(50)
B = randset(50)
C = randset(50)

# Create a Venn diagram with the sets
venn2((A, B), ('A', 'B'))

# Display the Venn diagram
plt.show()
