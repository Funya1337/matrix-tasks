import copy

n = int(input())

matrix = []

for i in range(n):
    line = list(map(int, input().split()))
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

def determinant():
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

def algAddition(m, i, j):
  summ = 0
  if len(m) == 2:
    return (m[0][0] * m[1][1]) - (m[0][1] * m[1][0])
  else:
    return ((-1)**(i + j)) * algAddition(minor(m, i, j), i - 1, j - 1)

transpone = transpone(matrix, n)
determinant = determinant()

for i in range(len(matrix)):
  for j in range(len(matrix)):
    transpone[j][i] = algAddition(matrix, i, j)

num = 1 / determinant

for i in range(len(transpone)):
  for j in range(len(transpone)):
    transpone[i][j] = num * transpone[i][j]

for i in transpone:
  print(*i)

