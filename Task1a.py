import copy

h = 0.1

a = 0
b = 0.8
c = 0
d = 0.8
N = int((b-a) / h)

def phi(x, y):
    return x**2 + y**2

def f():
    return -4

def p():
    return (1/h**2)/(2/h**2 + 2/h**2)

def F():
    return f()/(2/h**2 + 2/h**2)

def z_ij(i, j, z):
    return p()*(z[i-1][j] + z[i+1][j]) + p()*(z[i][j-1] + z[i][j+1]) + F()

def createMatrix():
    z = []
    for i in range(N+1):
        row = []
        for j in range(N+1):
            row.append(0)
        z.append(row)
    return z

def initMatrix(matrix):
    firstRow = matrix[0]
    for k in range(len(firstRow)):
        x = 0
        y = c + h*k
        firstRow[k] = phi(x, y)
    lastRow = matrix[-1]
    for k in range(len(lastRow)):
        x = 0.8
        y = c + h*k
        lastRow[k] = phi(x, y)

    for k in range(1, len(matrix)-1):
        row = matrix[k]
        x = a + k*h
        y = c + k*h
        row[0] = phi(x,0)
        row[-1] = phi(0.8, y)

def createPureSolutionMatrix():
    matrix = []
    for i in range(N+1):
        row = []
        for j in range(N+1):
            x = a + h*i
            y = c + h*j
            row.append(x**2 + y**2)
        matrix.append(row)
    return matrix

def findNorm(matrixOld, matrixNew):
    max = -1
    for i in range(N+1):
        for j in range(N+1):
            vault = abs(matrixOld[i][j] - matrixNew[i][j])
            if vault > max:
                max = vault
    return max

def fillFullMatrix(matrix):
    for i in range(1, N):
        for j in range(1, N):
            matrix[i][j] = z_ij(i, j, matrix)

def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"

def CustomPrint(A):
    for row in A:
        for elem in row:
            print(toFixed(elem, 5), end=' ')
        print()

if __name__ == "__main__":
    z = createMatrix()
    initMatrix(z)
    z1 = copy.deepcopy(z)
    fillFullMatrix(z)
    norm = findNorm(z, z1)
    while norm > h*h:
        z1 = copy.deepcopy(z)
        fillFullMatrix(z)
        norm = findNorm(z, z1)
    print("Решение")
    CustomPrint(z)
    matrix = createPureSolutionMatrix()
    print()
    print("Точное решение")
    CustomPrint(matrix)

    print()
    print("Погрешность:")
    print(findNorm(z, matrix))
    print()
    for i in range(len(z)):
        print(str(i)+")" + str([toFixed(z[i][j], 5) for j in range(len(z[i]))]))
        print(str(i)+")" + str([toFixed(matrix[i][j], 5) for j in range(len(matrix[i]))]))