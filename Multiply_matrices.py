def matrixmulti(X, Y):
    M = len(X)
    N = len(X[0])
    P = len(Y[0])
    
    Z = [[0] * P  for row in range(M)]
    
    if  N != len(Y):  
        print ("Incorrect dimensions.")
        return

    for i in range(M):
        for j in range(P):
            for k in range(N):
                Z[i][j] += X[i][k] * Y[k][j]

    return Z

A = [(1,2), (1,2)]
B = [(1,2), (1,2)]

C = matrixmulti(A,B)
for row in C:
    print(row)
