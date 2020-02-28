def fact(n):
  if n == 1:
    return 1
  return n*fact(n-1)

def combo(n, r):
  return fact(n)/(fact(r)*fact(n-r))

def sigma_combo(n, k, end):
  if k == end:
    return combo(n, end)
  return combo(n, k) + sigma_combo(n, k+1, end)

result = sigma_combo(64, 1, 32)
print(result)
