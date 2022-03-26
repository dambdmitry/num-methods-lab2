import math

h = 0.1

a = 0
b = 0.8
c = 0
d = 0.8
l = b - a
N = int((b - a) / h)


def phi(i, j):
    x = a + h * i
    y = c + h * j
    return x ** 2 + y ** 2


def f():
    return -4


def createMatrix():
    z = []
    for i in range(N + 1):
        row = []
        for j in range(N + 1):
            row.append(0)
        z.append(row)
    return z


def initMatrix(matrix):
    firstRow = matrix[0]
    for k in range(len(firstRow)):
        firstRow[k] = phi(0, k)
    lastRow = matrix[-1]
    for k in range(len(lastRow)):
        lastRow[k] = phi(N, k)

    for k in range(1, len(matrix) - 1):
        row = matrix[k]
        row[0] = phi(k, 0)
        row[-1] = phi(k, N)


def createPureSolutionMatrix():
    matrix = []
    for i in range(N + 1):
        row = []
        for j in range(N + 1):
            x = a + h * i
            y = c + h * j
            row.append(x ** 2 + y ** 2)
        matrix.append(row)
    return matrix


def findNorm(matrixOld, matrixNew):
    max = -1
    for i in range(N + 1):
        for j in range(N + 1):
            vault = abs(matrixOld[i][j] - matrixNew[i][j])
            if vault > max:
                max = vault
    return max


def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"


def CustomPrint(A):
    for row in A:
        for elem in row:
            print(toFixed(elem, 5), end=' ')
        print()


def createFMatrix():
    res = []
    for i in range(N + 1):
        row = []
        for j in range(N + 1):
            if i == 0 or i == N:
                row.append(0)
                continue
            if j == 0 or j == N:
                row.append(0)
                continue
            row.append(f())
        res.append(row)
    return res


def transformToMagicF(fMatrix):
    for i in range(1, N):
        for j in range(1, N):
            if 1 < i < N - 1 and 1 < j < N - 1:
                continue
            else:
                topDistance = i
                botDistance = N - i
                leftDistance = j
                rightDistance = N - j
                minDistance = min(topDistance, botDistance, leftDistance, rightDistance)
                summa = 0
                if minDistance == topDistance:
                    summa += phi(0, j) / (h * h)
                if minDistance == botDistance:
                    summa += phi(N, j) / (h * h)
                if minDistance == leftDistance:
                    summa += phi(i, 0) / (h * h)
                if minDistance == rightDistance:
                    summa += phi(i, N) / (h * h)
                fMatrix[i][j] = f() + summa


def m_k(k):
    return (4 / (h * h)) * math.sin(math.pi * k * h / (2 * l))**2


def createLambdas():
    lamdas = createMatrix()  # матрица из нулей
    for i in range(1, N):
        for j in range(1, N):
            lamdas[i][j] = m_k(i) + m_k(j)
    return lamdas


def v_jk(j, k):
    return math.sqrt(2 / l) * math.sin(math.pi * k * h * j / l)


def w(k1, k2, i, j):
    return v_jk(i, k1) * v_jk(j, k2)


if __name__ == "__main__":
    fMatrix = createFMatrix()  # шаг первый
    transformToMagicF(fMatrix)  # шаг второй
    lambdas = createLambdas()  # шаг третий
    # шаг четвертый - не нужон он ваш шаг четвортый | функция w - это решает
    # Шаг пятый
    cMatrix = createMatrix()  # матрица из нулей
    for k1 in range(1, N):
        for k2 in range(1, N):
            summa = 0
            for i in range(1, N):
                for j in range(1, N):
                    summa += fMatrix[i][j] * w(k1, k2, i, j)
            cMatrix[k1][k2] = summa * h * h / lambdas[k1][k2]
    # Шаг шестой
    z = createMatrix()
    initMatrix(z)
    for i in range(1, N):
        for j in range(1, N):
            summa = 0
            for k1 in range(1, N):
                for k2 in range(1, N):
                    summa += cMatrix[k1][k2] * w(k1, k2, i, j)
            z[i][j] = summa

    print("Метод сеток с методом  Фурье для разностных уравнений")
    CustomPrint(z)
    matrix = createPureSolutionMatrix()
    print()
    print("Точное решение")
    CustomPrint(matrix)

    print()
    for i in range(len(z)):
        print(str(i) + ")" + str([toFixed(z[i][j], 5) for j in range(len(z[i]))]))
        print(str(i) + ")" + str([toFixed(matrix[i][j], 5) for j in range(len(matrix[i]))]))
