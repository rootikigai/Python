"""
PseudoCode
Create new scanner called input
Initialize variables: p, m, r and n (where they respectively mean Principal, Monthly payments value, Annual Interest Rate and Loan duration) and assign value 0
collect input for p
collect input for r
initialize constant variable monR (to store the monthly rate value) and assign value of rate in decimals divided by 12 months.
collect input for n
initialize constant variable monN (to store value for number of months in the number of years entered) and assign value of n multiplied by 12 months
check if rate inputted is 0 to avoid divisible by 0 error else, do the math.
build formula for the value of m: 
go back to the method body and declare variables num for numerator and denom for denominator
numerator: Principal value multiplied by monthly rate multiplied by the value of 1 + monthly rate raised to the power of the loan duration in months
denominator: the value of 1 + monthly rate raised to the power of the loan duration in months, all minus 1
outside the else statement, calculate for m: m is equal to num divided by denom
print the value of m
"""

import math
