
from timer import timeit

def reverse1(s: str) -> str:
  rl = []
  for e in s:
    rl = [e] + rl
  return "".join(rl)
  
def reverse2(s: str) -> str:
  rl = []
  for i in range(len(s)- 1, -1, -1):
    rl.append(s[i])
  return "".join(rl)

def reverse3(s: str) -> str:
  rl = [l for l in s] 
  rl.reverse()
  return "".join(rl)

def reverse4(s: str) -> str:
  if len(s) <= 1:
    return s
  return s[-1] + reverse4(s[1:-1]) + s[0] 