from sys import stdin

def solve(target):
  ans = None
  # edit here
  return ans

def main():
  target = [int(x) for x in stdin.readline().strip().split()]
  while target[0]!=1 or target[1]!=1:
    print(solve(target))
    target = [int(x) for x in stdin.readline().strip().split()]

main()
