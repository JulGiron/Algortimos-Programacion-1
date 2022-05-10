
import Lists
from Lists.largest_number import find_max
from Lists.list_merge import merge

import Brute_force
from Brute_force.sum_of_first_n_numbers import sum_first_numbers
from Brute_force.pin_unlock import unlock
from Brute_force.divisor_of_n import divisors

import Recursion
import sys
sys.setrecursionlimit(2000)
from Recursion.sum_first_n_numbers_recursive import sum_of_n
from Recursion.fibonacci_number import fibonacci_sequence
from Recursion.factorial_of_n  import factorial
from Recursion.countdown import countdown

import Sorting
from Sorting.bubble_sort import bubble_sort
from Sorting.selection_sort import selection_sort
from Sorting.bubble_sort_optimized import bubble_sort_optimized
from Sorting.insertion_sort import insertion_sort

import Searching
from Searching.linear_search import linear_search
from Searching.binary_search import binary

print("¡Bienvenidos a todos a los algoritmos realizados en programación I! Este es el modulo de testing, sientanse en confianza de correrlo!")

print("----------------------------| #1: LARGEST NUMBER IN A LIST |----------------------------  ")
print("")

arr=[2, 5, 1, 7, 10]
find_max(arr)
print("El número más grande en la lista es: ",find_max(arr))

print("")

print("----------------------------| #2: LIST MERGE |------------------------------------------- ")
print("")

lista1=[1,4,9]
lista2=[2,3,8]
merge(lista1, lista2)

print("")

print("---------------------------| #3: SUM OF FIRST N NUMBERS |-------------------------------- ")
print("")

n=input("Ingrese un número natural: ")
n=int(n)
print("Numero ingresado: ",n)
sum_first_numbers(n)

print("")

print("---------------------------| #4: 4-DIGIT PIN UNLOCK |----------------------------------- ")
print("")

print(unlock("1000"))

print("")

print("---------------------------| #5: SUM OF FIRST N NUMBERS (RECURSION) |------------------- ")
print("")

print("n = 1000")
print("Sum of n:",sum_of_n(1000))

print("")

print("---------------------------| #6: FIBONACCI NUMBER |--------------------------------- ")
print("")

print("Fibonacci Number:",fibonacci_sequence(32))

print("")

print("---------------------------| #7: FACTORIAL OF N |--------------------------------------- ")
print("")

print("El factorial es:",factorial(5))

print("")

print("---------------------------| #8: COUNTDOWN |------------------------------------------- ")
print("")

print(countdown(5))

print("")

print("---------------------------| #9: BUBBLE SORT |-------------------------------------------")
print("")

lista=[-2,45,0,11,-9]
print("Lista desordenada: ", lista)
sorted_list=bubble_sort(lista)
print("Lista ordenada: ",sorted_list)

print("")

arr = [9, 5, 4, 7, 10, 14, 15, 13, 8, 2]
arr2 = [8, 5, 7, 8, 9, 10, 5 ,7, 3, 2]

print("---------------------------| #10: SELECTION SORT |---------------------------------------")
print("")

print(selection_sort(arr))

print("")

print("---------------------------| #11: BUBBLE SORT OPTIMIZED  |-------------------------------")
print("")

print(bubble_sort_optimized(arr))

print("")

print("---------------------------| #12: INSERTION SORT |---------------------------------------")
print("")

print(insertion_sort(arr))

print("")

print("---------------------------| #13: LINEAR SEARCH |----------------------------------------")
print("")

if linear_search(arr2,4) == -1:
    ans = "El número no se encuentra en la lista"
else:
    ans = "El número se encuentra en el indice: ",linear_search(arr2,4)
print(ans)

print("")

print("---------------------------| #14: BINARY SEARCH |---------------------------------------")
print("")

if binary(arr,4) == -1:
    respuesta = "El número no se encuentra en la lista"
else:
    respuesta = 'El número se encuentra en el indice:',binary(arr,4)

print(respuesta)

print("")

print("---------------------------| #15: DIVISORS OF N |----------------------------------------")
print("")

n = 8937222
result = divisors(n)
print("N: " + str(n) + " Divisors: " + str(result) )

print("")     


