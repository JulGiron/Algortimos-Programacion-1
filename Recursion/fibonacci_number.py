
def fibonacci_sequence(n_param):

    n = n_param

    if n == 0: 
        return 0
    
    if n == 1: 
        return 1
    return fibonacci_sequence(n - 1) + fibonacci_sequence(n-2)




