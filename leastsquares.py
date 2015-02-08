# doesn't do integer division for 1/2
from __future__ import division 
from sympy import *

# solve for where least squares intercepts the origin
# so mu = Bx minimizes sum[(Yi - Bxi)^2]
a,b,u,mu,y,i,n = symbols('a,b,u,mu,y,i,n');
f = (a-b)**2
g = Sum(f,(i,0,n))
expr = expand((a-b)**2)






# little trickery: replace a with y-mu and b with mu-u
# the mu is our solution
e = expr.subs(a,(y-mu)).subs(b,(mu-u))

# e = (-mu + y)**2 - 2*(-mu + y)*(mu - u) + (mu - u)**2
# the first and last expressions are squared, so we want 
# to look at the middle one and make that as small as possible
k = e.args[2]
k = k/-2 # doesn't matter
B,B_,x = symbols('B,B_,x')
k1 = k.subs([(mu,B_*x),(u,B*x)]) # (-B*x + B_*x)*(-B_*x + y)
k2 = collect(k1,x)    # -Bx**2 + Bx*u + Bx*y - u*y ???
# sum(-Bx+y) = 0
# 
# Bx^ = y^ is one solution, e.g. B
# B = y^/x^?
# 
