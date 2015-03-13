
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
    
   def simpson(self,f,a,b,n):
        self.x=numpy.linspace(a,b,n+1)
        y=f(self.x)
    
        h = float(self.x[1] - self.x[0])
        n = len(self.x) - 1
        if n % 2 == 1:
            n -= 1
        s = y[0] + y[n] + 4.0 * sum(y[1:-1:2]) + 2.0 * sum(y[2:-2:2])
        return h * s / 3.0
    
    
  
    
