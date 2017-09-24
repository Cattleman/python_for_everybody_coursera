# Binomial Tree for America and European options
# Author: Mehdi Bounouar,
# http://www.volopta.com/ComputerCode/Python_Other/BinomialTree_CRR_py.txt
# The code is inspired from:
# [S.R Das, B. Ganger, Journal of Investment Management, Vol.9, No.4, (2010), pp.73-84]
# and the C++ code version from Volopta written by Dr. F. Rouah


import numpy as np


def BinomialTreeCRR(n, Spot, k, r, v, T, PutCall, OpStyle):
    """
    n: steps
    Spot: Spot price
    K: Strike price
    r: Risk free rate
    v: volatility
    T: Maturity
    PutCall: European or American
    OpStyle: Call or Put
    """
    dt = T/n
    u = np.exp(v*np.sqrt(dt))
    d = 1./u
    p = (np.exp(r*dt)-d)/(u-d)
    
    #Binomial price tree
    stkval = np.zeros((n+1,n+1))
    stkval[0,0] = Spot
    for i in range(1,n+1):
        stkval[i,0] = stkval[i-1,0]*u
        for j in range(1,i+1):
            stkval[i,j] = stkval[i-1,j-1]*d
    
    #option value at each final node
    optval = np.zeros((n+1,n+1))
    for j in xrange(n+1):
        if PutCall=="C": # Call
            optval[n,j] = max(0, stkval[n,j]-k)
        elif PutCall=="P": #Put
            optval[n,j] = max(0, k-stkval[n,j])
    
    #backward recursion for option price
    for i in xrange(n-1,-1,-1):
        for j in xrange(i+1):
            if OpStyle=="E":
                optval[i,j] = np.exp(-r*dt)*(p*optval[i+1,j] + (1-p)*optval[i+1,j+1])
            elif OpStyle=="A":
                if PutCall=="P":
                    optval[i,j] = max(k-stkval[i,j], np.exp(-r*dt)*(p*optval[i+1,j]+(1-p)*optval[i+1,j+1]))
                elif PutCall=="C":
                    optval[i,j] = max(stkval[i,j]-k, np.exp(-r*dt)*(p*optval[i+1,j]+(1-p)*optval[i+1,j+1]))
    return optval[0,0]


if __name__ == "__main__":
    Spot = 100.           # Spot Price
    k = 99.               # Strike Price
    r = .05               # Annual Risk-free rate
    v = .2575             # Annual Volatility
    T = 200./(365)        # Time in year (days/365)
    n = 4                 # Number of steps

    #OpType 'C' = Call and 'P' = Put
    #ExType 'A' = American and 'E' = European

    print "CRR Binomial Prices:"
    print "American Put: %s" %(BinomialTreeCRR(n, Spot, k, r, v, T, PutCall="P", OpStyle="A"))
    print "American Call: %s" %(BinomialTreeCRR(n, Spot, k, r, v, T, PutCall="C", OpStyle="A"))
    print "European Put: %s" %(BinomialTreeCRR(n, Spot, k, r, v, T, PutCall="P", OpStyle="E"))
    print "European Call: %s"%(BinomialTreeCRR(n, Spot, k, r, v, T, PutCall="C", OpStyle="A"))
#   print BinomialTreeCRR(n, Spot, k, r, v, T, PutCall="P", OpStyle="A")