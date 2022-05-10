
def sum_of_n(n_param):

    n=n_param

    if n == 1: 
        return 1
    
    else: 
        return n + sum_of_n(n - 1)




