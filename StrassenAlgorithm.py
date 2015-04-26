__author__ = 'WangZhe'

# File: StrassenAlgorithm.py
# Description: This script implement the Strassen's matrix multiplying
#               algorithm, which is an example of divide and conquer.
# Start: 04/08/2015 20:51
# Finish: 04/08/2015 21:43
# After Debugging 04/08/2015 22:49\

def myPlus(a, b):
    n = len(a)
    res = [[a[i][j] + b[i][j] for j in range(n)] for i in range(n)]
    return res

def myMinus(a, b):
    n = len(a)
    res = [[a[i][j] - b[i][j] for j in range(n)] for i in range(n)]
    return res


def Strassen(x, y):
    n = len(x) #    dimension of matrix
    result = [[0 for i in range(n)] for i in range(n)]
    if n == 2:
        a = x[0][0]
        b = x[0][1]
        c = x[1][0]
        d = x[1][1]
        e = y[0][0]
        f = y[0][1]
        g = y[1][0]
        h = y[1][1]
        result[0][0] = a*e+b*g
        result[0][1] = a*f+b*h
        result[1][0] = c*e+d*g
        result[1][1] = c*f+d*h
        return result
    else:
        newDim = n//2
        A = [[x[j][i] for i in range(newDim)] for j in range(newDim)]
        B = [[x[j][i+newDim] for i in range(n-newDim)] for j in range(newDim)]
        C = [[x[j+newDim][i] for i in range(newDim)] for j in range(n-newDim)]
        D = [[x[j+newDim][i+newDim] for i in range(n-newDim)] for j in range(n-newDim)]
        E = [[y[j][i] for i in range(newDim)] for j in range(newDim)]
        F = [[y[j][i+newDim] for i in range(n-newDim)] for j in range(newDim)]
        G = [[y[j+newDim][i] for i in range(newDim)] for j in range(n-newDim)]
        H = [[y[j+newDim][i+newDim] for i in range(n-newDim)] for j in range(n-newDim)]
        FminusH = myMinus(F, H)
        P1 = Strassen(A, FminusH)
        AplusB = myPlus(A, B)
        P2 = Strassen(AplusB, H)
        CplusD = myPlus(C, D)
        P3 = Strassen(CplusD, E)
        GminusE = myMinus(G, E)
        P4 = Strassen(D, GminusE)
        AplusD = myPlus(A, D)
        EplusH = myPlus(E, H)
        P5 = Strassen(AplusD, EplusH)
        BminusD = myMinus(B, D)
        GplusH = myPlus(G, H)
        P6 = Strassen(BminusD, GplusH)
        AminusC = myMinus(A, C)
        EplusF = myPlus(E, F)
        P7 = Strassen(AminusC, EplusF)

        leftup = myMinus(myPlus(myPlus(P5, P6), P4), P2)
        rightup = myPlus(P1, P2)
        leftdown = myPlus(P3, P4)
        rightdown = myMinus(myPlus(P1, myMinus(P5, P7)), P3)

        res = [[0 for i in range(n)] for i in range(n)]
        for i in range(n):
            for j in range(n):
                if i < newDim:
                    if j < newDim:
                        res[i][j] = leftup[i][j]
                    else:
                        res[i][j] = rightup[i][j-newDim]
                else:
                    if j < newDim:
                        res[i][j] = leftdown[i-newDim][j]
                    else:
                        res[i][j] = rightdown[i-newDim][j-newDim]
        return res

x = [[i*j+j for j in range(1, 17, 1)] for i in range(1, 17, 1)]
y = [[i*j+j for j in range(1, 17, 1)] for i in range(1, 17, 1)]
print(Strassen(x, y))