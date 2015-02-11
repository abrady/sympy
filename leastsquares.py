from __future__ import division
from sympy import *
x, y, z, t = symbols('x y z t')
k, m, n = symbols('k m n', integer=True)
f, g, h = symbols('f g h', cls=Function)
init_printing()


# solve for where least squares intercepts the origin
# so mu = Bx minimizes sum[(Yi - Bxi)^2]
# Sum[(y[i] - B*x[i])**2]
x,y,B1,B1_,i,n = symbols('x,y,B1,B1_,i,n')
f0 = (Indexed(y,i)-B1*Indexed(x,i))**2
f1 = expand(Sum(f0,(i,0,n))) # Sum(B1**2*x[i]**2, (i, 0, n)) + Sum(-2*B1*x[i]*y[i], (i, 0, n)) + Sum(y[i]**2, (i, 0, n))

# Sum(-2*B1*x[i]*y[i], (i, 0, n)) is the expression we care about. the other two are squared, so always positive, if we can make this one zero we know we have the smallest possible value (unless negative?)
f2 = f1.args[2] # middle expression is in arg2 for some reason

#f2 = g.args[2] # Sum(-2*a*b, (i, 0, n))








# little trickery: replace a with y-mu and b with mu-u
# the mu is our solution
#e = expr.subs(a,(y-mu)).subs(b,(mu-u))

# e = (-mu + y)**2 - 2*(-mu + y)*(mu - u) + (mu - u)**2
# the first and last expressions are squared, so we want 
# to look at the middle one and make that as small as possible
#k = e.args[2]
#k = k/-2 # doesn't matter
#B,B_,x = symbols('B,B_,x')
#k1 = k.subs([(mu,B_*x),(u,B*x)]) # (-B*x + B_*x)*(-B_*x + y)
#k2 = collect(k1,x)    # -Bx**2 + Bx*u + Bx*y - u*y ???
# sum(-Bx+y) = 0
# 
# Bx^ = y^ is one solution, e.g. B
# B = y^/x^?
# 
