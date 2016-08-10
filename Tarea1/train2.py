from sys import stdin

MAX = 25010
train = [ None for i in range(MAX) ]

def solve(n):
  swapps=0
  for i in range(n-1):
    for j in range (i,n):
      if train[i]>train[j]:
        train[i],train[j]=train[j],train[i]
        swapps=swapps+1
  return swapps

def main():
  global train
  inp = stdin
  cases = int(inp.readline().strip())
  while cases>0:
    n = int(inp.readline().strip())
    tok = inp.readline().strip().split()
    for i in range(n): train[i] = int(tok[i])
    print('Optimal train swapping takes {0} swaps.'.format(solve(n)))
    cases -= 1

main()
