'''
Class Interpolate:
 
    def solve(self,L,M,method):
        if(method=="newton"):
            return (self.Newton(L,M))
        else:
            return (self.Lagrange(L,M))

    def Lagrange(self,L,M):                                                
       
        
        from numpy import array
        from numpy.polynomial import polynomial as P
        n=len(L)                                                           
        x=(-1*L[0],1)                                                      
        for i in range(1,n):
            x=P.polymul(x,(-1*L[i],1))                                    
        result=array([0.0 for i in range(len(x)-1)])                    
        derivative=P.polyder(x)                                             
        for i in range(n):
            result+=(P.polydiv(x,(-1*L[i],1))[0]*M[i])/P.polyval(L[i],derivative)   
        return(list(result))   
    def Newton(self,L,M):                                                   
       
        
        from numpy import array
        from numpy.polynomial import polynomial as P
        n=len(L)                                                            
        mat=[[0.0 for i in range(n)] for j in range(n)]                    
        for i in range(n):                                                 
            mat[i][0]=M[i]
        for i in range(1,n):                                               
            for j in range(n-i):
                mat[j][i]=(mat[j+1][i-1]-mat[j][i-1])/(L[j+i]-L[j])
        result=array((mat[0][0],))                                          
        for i in range(1,n):
            prod=(-1*L[0],1)                                               
                                                                            
            for j in range(1,i):
                prod=P.polymul(prod,(-1*L[j],1))                              
            result=P.polyadd(result,array(prod)*mat[0][i])                  
        return (list(result))                                               

apx=Interpolate()                                                          
for method in ["newton","lagrange"]:
    solution=apx.solve([1,2,3],[0,-1,0],method)
    print(solution)
'''
import sympy as sp
import matplotlib.pyplot as plt
import numpy as np
class Interpolate:
    S, Q, R = [], [], []
    # for finding limits, polynomials
    x = sp.Symbol('x')
    def Lag_Poly(self, L, M):
        # X for storing x coordinates
        # Y for storing f(x)
        self.Q, self.R = L, M
        for i in range(len(L)):
            u, j = 1, 0
            # forming list of polynomials
            # summation of which is Lagrange Polynomial
            while j < len(L):
                if i != j:
                    u *= (self.x-L[j])/(L[i]-L[j])
                j += 1   
            u*= M[i] 
            self.S.append(u)
        # plot Lagrange Polynomial
        self.plot_Poly()      
    
    def plot_Poly(self, var = []):
        a = np.arange(0,max(self.Q)+0.2,0.1)
        pol_sum = 0
        # plot function in the list
        for  i in self.S:
            pol_sum += i
            for j in a:
                var.append(sp.limit(i,self.x,j))
            plt.plot(a, var)             
            var = []       
        # plot Lagrange Polynomial in Black Color
        for j in a:
                var.append(sp.limit(pol_sum,self.x,j))
        plt.plot(a, var,'k')
        # plot node points
        plt.plot(self.Q,self.R,'ro')
        plt.title('INTERPOLATING POLYNOMIAL IS BLACK')
        plt.xlabe('X-AXIS')
        plt.ylabel('Y-AXIS')
        plt.show()              
