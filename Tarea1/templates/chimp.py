from sys import stdin

def solve(ladies,x):
  # edit here
  pass

def main():
  stdin.readline()
  ladies = [ int(x) for x in stdin.readline().split() ]
  stdin.readline()
  queries = [ int(x) for x in inp.readline().split() ]
  for x in queries:
    solve(ladies, x)

main()
