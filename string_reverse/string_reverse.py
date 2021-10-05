
from timer import timeit

@timeit
def reverse1(s: str) -> str:
  rl = []
  for e in s:
    rl = [e] + rl
  return "".join(rl)
  
@timeit
def reverse2(s: str) -> str:
  rl = []
  for i in range(len(s)- 1, -1, -1):
    rl.append(s[i])
  return "".join(rl)

@timeit
def reverse3(s: str) -> str:
  rl = s.split()
  rl.reverse()
  return "".join(rl)