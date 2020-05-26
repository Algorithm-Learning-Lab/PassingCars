
def solution(A) :
  result = 0
  n = len(A)

  if (n < 1 or n > 100000) :
    return print("result: range error")

  for i in range(n) :
    if A[i] != 0 and A[i] != 1 :
      return print("result: range error")



  PSum = [0] * (n+1)

  for k in range (1, n+1) :
    PSum[k] = PSum[k-1] + A[k-1]

  for k in range (0, n) :
    if A[k] == 0 :
      result += (PSum[n] - PSum[k+1])
    if result > 1000000000 :
      result = -1
      break

  print("result:", result)



A = list(map(int, input("insert array A : ").split()))

solution(A)
