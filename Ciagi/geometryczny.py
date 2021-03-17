def nty(a1, n, q):
    an = a1 * (q**(n-1))
    return an
def suma(a1, n, q):
    if q != 1:
        sn = (a1 * (1-(q**n)))/(1-q)
    else:
        sn = n * a1
    return sn