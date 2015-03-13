#ONLY METHODS TO FIND ROOTS OF A POLYNOMIAL

#example :
#bisect(array of coeffecients of polynomial,starting point,endpoint)
def bisect(a, low, high):
         func=lambda x: sum([(x**(len(a)-a.index(i)-1))*i for i in a])
         def samesign(a,b):
             return a*b>0
         for i in range(54):
                midpoint = (low + high) / 2.0
                if samesign(func(low), func(midpoint)):
                     low = midpoint
                else:
                     high = midpoint
         return midpoint
#bisect(array of coeffecients of polynomial,starting point,endpoint)       
def secant_solve(a,x1,x2):
        import sys
        f=lambda x: sum([(x**(len(a)-a.index(i)-1))*i for i in a])
        ftol,xtol= 0.000001, 0.000001
        f1 = f(x1)
        if abs(f1) <= ftol : return x1        # already effectively zero
        f2 = f(x2)
        if abs(f2) <= ftol : return x2
        while abs(x2 - x1) > xtol :
            slope = (f2 - f1)/(x2 - x1)
            if slope == 0 :
                sys.stderr.write("Division by 0 due to vanishing slope - exit!\n")
                sys.exit(1)
            x3 = x2 - f2/slope               # the new approximate zero
            f3 = f(x3)
            if abs(f3) <= ftol : break
            x1,f1 = x2,f2                    # copy x2,f2 to x1,f1
            x2,f2 = x3,f3 
        return x3
#bisect(array of coeffecients of polynomial,starting point, h close to zero,no of iterations)
def newton_raphson(a, x0, h, depth):
         f=lambda x: sum([(x**(len(a)-a.index(i)-1))*i for i in a])
         def derivative (f, x, h):
             return float((f(x + h) - f(x))) / h
         if depth > 0:
              delta = f(x0) / derivative(f, x0, h)
              return newton_raphson(a, x0 - delta, h, depth - 1)
         else:
             return x0
