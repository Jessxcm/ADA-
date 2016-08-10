from sys import stdin

def BisectionD(A,x):
    ans = 'X'
    N=len(A)
    if N>0 and A[0]<x :
      low,hi = 0,N
      while low+1!=hi:
        mid = low+((hi-low)>>1)
        if A[mid]<x:
          low = mid
        else:
          hi = mid
      ans = low
    return ans
def BisectionE(A,x):
    ans = 'X'
    N=len(A)
    if N>0 and A[0]<=x and A[N-1]>x:
      low,hi = 0,N
      while low+1!=hi:
        mid = low+((hi-low)>>1)
        if A[mid]>x:
          hi = mid
        else:
          low = mid
      ans = hi
    return ans

def solve(ladies,x):
    S1=BisectionD(ladies,x)
    S2=BisectionE(ladies,x)
    if S1=='X' and S2!='X':
        print(S1,ladies[S2],)
    elif S1!='X' and S2=='X':
        print(ladies[S1],S2)
    elif S1=='X' and S2=='X':
        print(S1,S2,)
    else:
        print(ladies[S1],ladies[S2],)
    pass

def main():
  stdin.readline()
  ladies = [ int(x) for x in stdin.readline().split() ]
  stdin.readline()
  queries = [ int(x) for x in stdin.readline().split() ]
  for x in queries:
    solve(ladies, x)

main()

