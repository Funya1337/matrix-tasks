import copy

n = int(input())

matrix = []
factors = []

for i in range(n):
    line = list(map(int, input().split()))
    factors.append(line[-1])
    del line[-1]
    matrix.append(line)

def minor(m, row, col):
  data_a = copy.deepcopy(m)
  del data_a[row]

  for i in range(len(data_a)):
    del data_a[i][col]
  return data_a

def transpone(matrix, size):
    res = []
    for i in range(size):
        line = []
        for j in range(size):
            line.append(matrix[j][i])
        res.append(line)
        line = []
    return res

def printMatrix(matrix):
    for i in matrix:
        print(*i)

def determinant(matrix):
  def f(data, col):
      data_a = copy.deepcopy(data)
      del data_a[0]

      for i in range(len(data_a)):
          del data_a[i][col]
      return data_a

  def rec(m):
    if len(m) == 2:
      return (m[0][0] * m[1][1]) - (m[0][1] * m[1][0])
    else:
      summ = 0
      for i in range(len(m)):
        mult = 1 if i % 2 == 0 else -1
        summ += (mult * m[0][i] * rec(f(m, i)))
      return summ
  res = rec(matrix)
  return res

def inverseMatrix():
    minorArray = [[0] * n for _ in range(n)]

    det = determinant(matrix)

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if len(matrix) == 2:
                res = minor(matrix, i, j)
                if (i % 2 != 0 and j % 2 == 0) or (i % 2 == 0 and j % 2 != 0):
                    minorArray[j][i] = -res[0][0]
                elif (i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0):
                    minorArray[j][i] = res[0][0]
            else:
                res = minor(matrix, i, j)
                res = determinant(minor(matrix, i, j))
                if (i % 2 != 0 and j % 2 == 0) or (i % 2 == 0 and j % 2 != 0):
                    minorArray[j][i] = -res
                elif (i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0):
                    minorArray[j][i] = res

    for i in range(len(minorArray)):
        for j in range(len(minorArray)):
            minorArray[i][j] = (1 / det) * minorArray[i][j]

    for i in range(len(minorArray)):
        for j in range(len(minorArray)):
            if minorArray[i][j] == int(minorArray[i][j]):
                minorArray[i][j] = int(minorArray[i][j])

    return minorArray

def SLAU():
    inverse = inverseMatrix()
    resArr = [[0] * n for _ in range(n)]
    ansArr = []
    for i in range(len(inverse)):
        summ = 0
        for j in range(len(inverse)):
            summ += (inverse[i][j] * factors[j])
        if abs(summ) < 10**-16:
            ansArr.append(0)
        else:
            if summ == int(summ):
                ansArr.append(int(summ))
            else:
                ansArr.append(summ)
    for i in range(len(resArr)):
        resArr[i][i] = 1

    for i in range(len(resArr)):
        resArr[i].append(ansArr[i])

    printMatrix(resArr)

SLAU()
