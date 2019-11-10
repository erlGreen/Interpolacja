import numpy as np


def lagrange(xvalues, yvalues, functionSequence):
    x = []
    y = []
    for k in range(0, int(xvalues[len(xvalues) - 1]/functionSequence) + 1):
       x.append(k * functionSequence)
       f = 0
       for i in range(0, len(yvalues)):
           fi = 1
           for j in range(0, len(xvalues)):
               if j != i:
                   fi = fi * (x[k] - xvalues[j])
                   fi = fi / (xvalues[i] - xvalues[j])
           f = f + yvalues[i] * fi
       y.append(f)
    return x, y


def splajn(xvalues, yvalues, functionSequence):
    h = xvalues[1] - xvalues[0]
    n = len(yvalues) - 1    #n = ilosc podprzedzialow
    A = np.zeros((4*n, 4*n), dtype=np.float)
    B = np.zeros((4*n, 1), dtype=np.float)
    for j in range(0, n):
        A[4*j][4*j] = 1 # 1 rownanie ustawienie tylko aj
        B[4*j][0] = yvalues[j]
        A[4*j+1][4*j] = 1 # 2 rownanie a
        A[4*j+1][4*j+1] = h # b
        A[4*j+1][4*j+2] = h*h # c
        A[4*j+1][4*j+3] = h*h*h # e
        B[4*j+1][0] = yvalues[j + 1]
        if j == 0:
            A[2][2] = 2
            B[2][0] = 0
            A[3][4*n - 2] = 2 #cn-1
            A[3][4*n - 1] = 6*h #dn-1
            B[3][0] = 0
        else:
            A[4*j+2][4*j-3] = 1 #bj-1 3 rownanie
            A[4*j+2][4*j-2] = 2*h #cj-1
            A[4*j+2][4*j-1] = 3*h*h #dj-1
            A[4*j+2][4*j+1] = -1 #bj
            A[4*j+3][4*j-2] = 2 # 4 rownanie cj-1
            A[4*j+3][4*j-1] = 6*h # dj-1
            A[4*j+3][4*j+2] = -2 # cj
    S = np.linalg.solve(A, B)
    x = []
    y = []
    xiterator = 0
    interval = 0
    for j in range(0, n):
        a = S[4*j][0]
        b = S[4*j+1][0]
        c = S[4*j+2][0]
        d = S[4*j+3][0]
        x0 = xvalues[j]
        interval = interval + h
        while xiterator <= interval:
            x.append(xiterator)
            y.append(a + b*(xiterator-x0) + c*(xiterator-x0)*(xiterator-x0) + d*(xiterator-x0)*(xiterator-x0)*(xiterator-x0))
            xiterator = xiterator + functionSequence
    return x, y


