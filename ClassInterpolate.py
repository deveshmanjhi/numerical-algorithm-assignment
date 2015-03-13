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
