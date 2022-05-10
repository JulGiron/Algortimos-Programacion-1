
lista=[-2,45,0,11,-9]

def bubble_sort(lista):

    for i in range (0,len(lista)):

        for j in range (0,len(lista)-1):

            if lista[j] > lista[j+1]:

                lista[j],lista[j+1]=lista[j+1],lista[j]

    return lista




