def strassen_2x2(A, B):

    a,b = A[0]
    c,d = A[1]

    e,f = B[0]
    g,h = B[1]

    M1 = (a+d)*(e+h)
    M2 = (c+d)*e
    M3 = a*(f-h)
    M4 = d*(g-e)
    M5 = (a+b)*h
    M6 = (c-a)*(e+f)
    M7 = (b-d)*(g+h)

    C11 = M1 + M4 - M5 + M7
    C12 = M3 + M5
    C21 = M2 + M4
    C22 = M1 - M2 + M3 + M6

    return [[C11,C12],[C21,C22]]


A = [[1,7],[3,5]]
B = [[1,3],[7,5]]

print(strassen_2x2(A,B))