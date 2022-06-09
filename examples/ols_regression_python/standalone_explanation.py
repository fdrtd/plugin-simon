import numpy as np


"""
random test data
"""

n = 100  # number of observations
p = 5  # number of independents

# random independent realizations
X = np.random.randint(100, size=(n, p))

# true coefficients are 1.0, 2.0, 3.0, ...
beta = [i+1 for i in range(p)]

# observations without error
Y0 = np.matmul(X, beta)

# some random errors
epsilon = np.random.randint(100, size=n)

# observations with noise
Y = np.add(Y0, epsilon)


"""
Non-private OLS regression requires knowledge of both X and Y.
MLEs are classically computed as beta = ((X^T * X)^-1 * X^T) * Y
"""

XT = X.transpose()

N = np.matmul(XT, X)

Ninv = np.linalg.inv(N)

MP = np.matmul(Ninv, XT)

MLE = np.matmul(MP, Y)

# this should give something similar to [1.0, 2.0, 3.0, ...] plus noise
print(MLE)


"""
Secure OLS regression requires knowledge of X by party A
and of Y by party B. A cannot simply sent its pseudoinverse MP
to B, as it contains some recoverable information about X.

See Alan F. Karr, Xiaodong Lin, Ashish P. Sanil (2007):
Privacy-Preserving Analysis of Vertically Partitioned Data Using Secure Matrix Products
"""


# First, A calculates the QR decomposition of MP^T
MPT = MP.transpose()
Q, R = np.linalg.qr(MPT, mode='complete')

# Of matrix Q, A needs g columns where g can be chosen as
g = int((p*n)/(p+1.0))

# Discarding the left p colums, A selects
Z = Q[:, p:p+g]

# Z is orthogonal and has the property Z^T_i * MPT_j = 0 for all i, j

# A computes V = 1-ZZ^T and sends V to B
V = np.identity(n) - np.matmul(Z, Z.transpose())

# B calculates W = V * Y and sends W to A
W = np.matmul(V, Y)

# A calculates MP * W which equals MP * Y, the desired result
MLE_secure = np.matmul(MP, W)

print(MLE_secure)
