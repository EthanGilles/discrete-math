'''
Author: Ethan Gilles
Date: 8/1/24
Class: COS280 - Discrete Math
Assignment: Lab 7
'''
import math

'''
Learning Objectives:
1. Work with sets in Python - 8 questions
2. Perform operations on sets in Python - 4 questions
3. Test for membership - 1 question
4. Test whether a set is a subset of another - 2 questions
5. Introduce dictionaries - 2 questions

Notes:
- All learning objectives have at least one question associated with them.
'''

'''
Question 1:
Enter the following sets into Python. Assign each to a variable (or label)
print(a)

LO's:
- Work with sets
'''

a = {"Red", "Green", "Blue"}

b = {2,3,4,6,5,1}

c = {2,3,3,4,5,6,1}

d = {1, 'fish', 2, 'fish', 'green fish', 'blue fish'}

'''
Question 2:
Loop over the elements of a set of colors above by accessing values directly 
(not using the range() function) to print the colors.

LO's:
- Work with sets
'''

# for color in a:
#     print(color)


'''
Question 3:
Create an empty set, a set with no elements, denoted mathematical as ∅
by typing set(). One may try to create using just {}. What happens? Use type()
to determine.

LO's 
- Work with sets
'''

e = set()
# print(type(e))


'''
Question 4:
Determine the truth of A = B and A = C. How would you guess to determine the
equality of two sets?

LO's:
- Work with sets
- Perform operations on sets
'''

A = {1,2,3}
B = {3,1,2}
C = {3,1,2,4,6,5}
D = {2,5}

AeqB = A == B
# print(AeqB)
AeqC = A == C
# print(AeqC)


'''
Question 5:
Determine the truth of the following: 2 ∈ A, 5 ∈ C, and 7 ∈ C

LO's:
- Work with sets 
- Test for membership
'''

x = 2 in A
y = 5 in C
z = 7 in C
# print(f"2 ∈ A - {x}    5 ∈ C - {y}    7 ∈ C - {z}")

'''
Question 6:
Determine whether A ⊆ B, A ⊆ C, and C ⊆ D.

LO's 
- Work with sets
- Perform operations on sets 
- Test whether one set is a subset of another
'''

x = A.issubset(B)
y = A <= C
z = C <= D
# print(f"A ⊆ B - {x}     A ⊆ C - {y}     C ⊆ D - {z}")


'''
Question 7:
Repeat #6 testing for proper subsets.

LO's 
- Work with sets
- Perform operations on sets 
- Test whether one set is a subset of another
'''

x = A < B
y = A < C
z = C < D
# print(f"A < B - {x}     A < C - {y}     C < D - {z}")


'''
Question 8:
Find the union, intersection, and difference of: A ∪ C, A ∩ C, and C ∖ D

LO's 
- Work with sets
- Perform operations on sets 
'''

x = A.union(C)
y = A.intersection(C)
z = C.difference(D)
# print(f"A ∪ C = {x}     A ∩ C = {y}      C ∖ D = {z}")


'''
Question 9:
Create a dictionary of "grades" that associate an 'A' with the value 90, 
'B' with 80, 'C' with 70, etc. How do you create an empty dictionary (see #3).

LO's
- Introduce dictionaries
'''

grades = {'A':90, 'B':80, 'C':70, 'D':60, 'F':50}
# print(grades)
empty = dict()
# print(type(empty))


'''
Question 10:
Loop over the items and print the dictionary (key - value pairs).

LO's:
- Introduce dictionaries
'''

areacodes = {'207':'Maine','213':'LA','304':'West Virginia','302':'LA','312':'LA'}

# for code, state in areacodes.items():
#     print(f"Area code for {state} is {code}")
