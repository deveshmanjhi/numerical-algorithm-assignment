#example :GaussJordan(matrix A,array of coefficients of equation)

from numpy import array, zeros, float, dot
from copy import copy

def GaussJordan(A,b):
    
    n,m = A.shape
    
    C = zeros((n,m+1),float)
    C[:,0:n],C[:,n] = A, b

    for j in range(n):
    
        p = j
        
        for i in range(j+1,n):
            if abs(C[i,j]) > abs(C[p,j]): p = i
        if abs(C[p,j]) < 1.0e-16:
            print "matrix is (likely) singular"
            return b 
        
        C[p,:],C[j,:] = copy(C[j,:]),copy(C[p,:])
        
        pivot = C[j,j]
        C[j,:] = C[j,:] / pivot
        for i in range(n):
            if i == j: continue
            C[i,:] = C[i,:] - C[i,j]*C[j,:]
    I,x = C[:,0:n],C[:,n]
    return x
