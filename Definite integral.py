
# ques 5
# usage: pass a function to be integrated,lower limit,upper limit,no of divisions
# example:b.trapezoid(lambda x:x,2,3,50)
import numpy

class Integrate():

  def trapezoid(self,f,a,b,n):
    
    self.x=numpy.linspace(a,b,n+1)
    y=f(self.x)
    s=y[0]+2.0*sum(y[1:n])+y[n]
    h=float(b-a)/n
    return s*h/2.0
    
    
  
    
