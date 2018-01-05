# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 12:33:34 2018

@author: iqbal
"""

"""
Functions pada segmen berikut ini akan menghasilkan urutan angka dari 1 s/d n
result : 1, 2, 3, 4, 5, 6, 7, 8, 9, ..., n

*******************************************************
INTEGER SEQUENCE FROM 1 TO 10 =========================
*******************************************************
ITERATIVE FUNCTION ==============================
"""
def integerSeqIterative(n):
    integer_sequence = []
    for i in range(1,n+1):
        integer_sequence.append(i)
    return integer_sequence

"""
=================================================
RECURSIVE FUNCTION ==============================
"""
def integerSeqRecursive(sequence, n):
    while n > 0:
            sequence.insert(0,n)
            return integerSeqRecursive(sequence, n-1)
    return sequence
            

print("=================================================")
print("CALLING INTEGER SEQUENCE FUNCTIONS ===============================")
print("hasil iterative ===============================")
print(integerSeqIterative(25))
print("hasil recursive ===============================")
print(integerSeqRecursive([],25))


"""
Functions pada segmen berikut ini akan mencari value pada posisi N di deret fibonacci
result: urutan ke n dari 0, 1, 1, 2, 3, 5, 8, 13, etc.
*******************************************************
N-TH NUMBER IN FIBONACCI ==============================
*******************************************************
ITERATIVE FUNCTION ==============================
"""
def fibSearchIterative(n):
    fibonacci = []
    i = 0
    while i <= n:
        if i == 0 or i == 1:
            fib = i
        else: 
            fib = fibonacci[i-1]+fibonacci[i-2]        
        fibonacci.append(fib)
        i += 1    
    return fibonacci[n]



"""
=================================================
RECURSIVE FUNCTION ==============================
"""
def fibSearchRecursive(fib_list, n):
    while len(fib_list) <= n:
        if len(fib_list) == 0 or len(fib_list) == 1:
            fib_list.append(len(fib_list))
        else:
            fib_list.append(fib_list[-1]+fib_list[-2])
        return fibSearchRecursive(fib_list, n)         
    return fib_list[-1]




print("=================================================")
print("CALLING FIBONACCI FUNCTIONS ===============================")
print("hasil iterative ===============================")
print(fibSearchIterative(0))
print(fibSearchIterative(1))
print(fibSearchIterative(2))
print(fibSearchIterative(3))
print(fibSearchIterative(4))
print(fibSearchIterative(5))
print(fibSearchIterative(150))
print("hasil recursive ===============================")
print(fibSearchRecursive([],0))
print(fibSearchRecursive([],1))
print(fibSearchRecursive([],2))
print(fibSearchRecursive([],3))
print(fibSearchRecursive([],4))
print(fibSearchRecursive([],5))
print(fibSearchRecursive([],150))

