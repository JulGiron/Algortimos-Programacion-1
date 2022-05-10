
def merge(lista1,lista2):
  
  
  print ("Lista 1: " + str(lista1))
  print ("Lista 2: " + str(lista2))
    
  len1 = len(lista1)
  len2 = len(lista2)
    
  lista_nueva = []
  i, j = 0, 0
    
  while i < len1 and j < len2:
      if lista1[i] < lista2[j]:
        lista_nueva.append(lista1[i])
        i += 1
    
      else:
        lista_nueva.append(lista2[j])
        j += 1
        
  lista_nueva = lista_nueva + lista1[i:] + lista2[j:]
    
  print ("Lista final ordenada: " + str(lista_nueva))




