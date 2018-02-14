def matrixMaker():
    A = []
    B = []
    print("")
    print("This calculator is based on the following logic: ")
    print("")
    print("A is a matrix with m rows and n columns, B is a matrix with n rows and p columns")
    print("")

    m = int(input("Rows in A --> "))
    n = int(input("Columns in A & Rows in B --> "))
    p = int(input("Columns in B --> "))

    matrixIndex = 1

    while matrixIndex <= 2:
        if matrixIndex == 1:
            print("")
            rowIndex = 1
            while rowIndex <= m:
                row = []
                colIndex = 1
                while colIndex <= n:
                    x = int(input("Integer in matrix A at " + str(rowIndex) + " X " + str(colIndex) + " --> "))
                    row.append(x)
                    colIndex += 1
                A.append(row)
                rowIndex += 1
        elif matrixIndex == 2:
            print("")
            rowIndex = 1
            while rowIndex <= n:
                row = []
                colIndex = 1
                while colIndex <= p:
                    x = int(input("Integer in matrix B at " + str(rowIndex) + " X " + str(colIndex) + " --> "))
                    row.append(x)
                    colIndex += 1
                B.append(row)
                rowIndex += 1
        else:
            break
        matrixIndex += 1
    print("")
    print(A)
    print("")
    print("*")
    print("")
    print(B)
    matrixMultiplier(A, B, m, n, p)

def matrixMultiplier(array1, array2, m, n, p):
    C = []
    a = 0
    while a < m:
        c = 0
        row = []
        while c < p:
            xc = 0
            b = 0
            while b < n:
                xc += (array1[a][b]*array2[b][c])
                b += 1
            row.append(xc)
            c += 1
        C.append(row)
        a += 1
    print("")
    print("=")
    print("")
    print(C)
    print("")
    repeat = input("Enter `yes` if you would like to multiply another pair of matrices; anything else will exit the application --> ")
    if repeat == "yes":
        matrixMaker()
    
matrixMaker()


