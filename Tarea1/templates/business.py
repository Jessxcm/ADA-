from sys import stdin

elevators,n,m = None,None,None

def solve():
  ans = float('inf')
  for u,d in elevators:
    #edit here
    pass
  return ans

def main():
  global elevators,n,m
  line = stdin.readline()
  while len(line)!=0:
    n,m = [ int(x) for x in line.split() ]
    elevators = [ [ int(x) for x in stdin.readline().split() ] for i in range(m) ]
    print(solve())
    line = stdin.readline()

main()
