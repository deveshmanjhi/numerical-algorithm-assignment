
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
        
        
    def simplot(self,f,a,b,n):
        x=np.arange(a,b,0.1)
        y=f(x)
        plt.plot(x,y,'r-')
        z=np.linspace(a,b,n)#divide interval in n parts
        g,h=[],[]
        i=0
        while i<len(z)-1:
            g.append((z[i]+z[i+1])/2.0)
            i=i+1
        
        for i in g:
            h.append(f(i))#corresponding y cordinates
        w=z[1]-z[0]#width
    
        v=z
        v=np.delete(v,len(v)-1)#delete the last cordinate
        plt.bar(v,h,width=w)
        for i,j in zip(g,h):
            plt.plot([i,i],[j,0],'r--')
        plt.title('INTEGRATION BY SIMPSONS METHOD')
        plt.xlabel('X-AXIS')
        plt.ylabel('Y-AXIS')
    
      def traplot(self,f,a,b,n):
        x=np.arange(a,b,0.1)
        y=f(x)
        plt.plot(x,y,'r-')
        z=np.linspace(a,b,n)
        y=[0]*n
        plt.plot(z,y,'bo-')
        plt.plot(z,f(z),'bo')
        c=f(z)
        for i,j in zip(z,c):
            plt.plot([i,i],[j,0],'bo-')
        plt.plot(z,f(z),'bo-')
        plt.title('INTEGRATION BY TRAPEZOIDAL METHOD')
        plt.xlabel('X-AXIS')
        plt.ylabel('Y-AXIS')    
       
        
    
        
    
    
  
    
