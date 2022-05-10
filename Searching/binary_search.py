
def binary(list,n):
    first = 0
    last = len(list)-1
    half = 0

    while first <= last :
        half = int((first + last)/ 2)
     
        if n == list[half]:
            return half

        elif n < list[half]:
            last = half - 1
          
        else:
            first = half + 1   
    return -1


