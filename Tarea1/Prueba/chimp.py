from sys import stdin

def BisectionD(A,x):
    N=len(A)
    ans ='X'
    if N>0 and A[N-1]>=x:
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
    ans='X'
    N=len(A)
    if N>0 and A[N-1]>x:
        low,hi=0,N
        while low+1!=hi:
            mid = low+((hi-low)>>1)
            if A[mid]>x:
                hi=mid
            else:
                low=mid
        ans=hi
    return ans

def solve(ladies,x):
    Menor=BisectionD(ladies,x)
    Mayor=BisectionE(ladies,x)
    return Menor,Mayor


A= [1,4,5,7]
x=3
B,C=solve(A,x)
print B,C


