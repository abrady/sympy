# init_session()
# These commands were executed:
from __future__ import division
from sympy import *
x, y, z, t = symbols('x y z t')
k, m, n = symbols('k m n', integer=True)
f, g, h = symbols('f g h', cls=Function)
init_printing()


# http://docs.sympy.org/latest/tutorial/intro.html
from sympy import *
a,b,u,mu,y = symbols('a,b,u,mu,y');
z_i = Indexed('z',i)
z = IndexedBase('z')
z2_i = z[i] # for some reason the recommended way to create indexed...
z3_i = symbols('z_i')
z_i == z2_i == z3_i
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
Sum(Indexed('x',i),(i,1,3)) # indexed x
Sum(Indexed('x',i),(i,1,3)).doit() # x[1] + x[2] + x[3]
Sum(x(i),(i,1,3)).doit() # x(1) + x(2) + x(3)

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
