
import numpy as np
import scipy.linalg as la
import matplotlib.pyplot as plt


# hbar is the Planks constant divided by pi
# m is the rest mass of the electron
hbar = 6.582119514
m = 5.11


# Specify the the spatial Dimension steps
nX = 1000

# Boundary conditions of X
xBound = [-1, 1]

# Spreading the X values bteween the boundary values
xVec = np.linspace(xBound[0], xBound[1], nX)
deltaX = np.abs( xVec[1] - xVec[0] )

# Laplacian operator matrix form using f(X+deltaX) - 2*f(x) + f(X-deltaX)
lapOperator = ( np.diag(np.ones(nX - 1), -1) - 2 * np.diag(np.ones(nX)) +
    np.diag(np.ones(nX - 1), 1) )/(float)( deltaX**2 )

# Potential function V(X)
potentialX = 0. * xVec

# Hamiltonian operator as K.E + P.E
hamiltonian = -( 1/(2*m) )*( hbar**2) * lapOperator + np.diag ( potentialX )

energy, psi  = la.eigh( hamiltonian )



