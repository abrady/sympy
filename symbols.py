# doesn't do integer division for 1/2
from __future__ import division 

# http://docs.sympy.org/latest/tutorial/intro.html
from sympy import *
a,b,u,mu,y = symbols('a,b,u,mu,y');
expr = (a-b)**2
e = expr.replace(a,(y-mu))
e = e.replace(b,(mu-u))

# we want to know when this is zero
# can also pass list of pairs: expr.subs([(x, 2), (y, 4), (z, 0)])
# replace vs subs?
k = (2*a*b).subs(a,(y-mu)).subs(b,(mu-u))

cmp = Eq(x+1,4)
cmp2 = cmp.subs(x,100) # False
cmp3 = cmp.subs(x,3)   # True

a = (x + 1)**2
b = x**2 + 2*x + 1
a == b # False
c = simplify(a - b)
Eq(c,0) # True
c == 0  # True
a.equals(b) # True

# Note: ^ and /x
# ^ is xor
x,y = var('x,y')
x^y
# Xor(x,y)

x = x+1/2 # careful! tured into x+.5 (or + 0)
# do this instead:
y = y + Rational(1,2)

expr = sympify('a**2+bx+c')

# evalf: get numeric value out

# calculus
###### 
i = symbols(i)
summation(1/2**i, (i,0,oo)) # solves summation
Sum(1/2**i, (i,0,oo))

# simplification
#################
expr = x**2+2*x+1
simplify(expr) # wrong!
factor(expr) # does what you want
expand((x+1)*(x-3))

x,y,z = symbols('x,y,z')
expr = x*y + x - 3 + 2*x**2 - z*x**2 + x**3
collect(expr, x) # x**3 + x**2*(-z + 2) + x*(y + 1) - 3

# cancel: cancels p/q
# apart: partial fraction decomp
# factorial
# binomial
