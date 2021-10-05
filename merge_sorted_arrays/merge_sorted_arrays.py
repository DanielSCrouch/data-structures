from timer import timeit

@timeit
def merge_sorted_arrays1(a1: list, a2: list) -> list:
  joined = a1 + a2
  joined.sort()
  return joined

@timeit
def merge_sorted_arrays2(a1: list, a2: list) -> list:
  joined = []

  i = 0 
  j = 0
  while True:

    if a1[i] < a2[j]:
      joined.append(a1[i])
      i += 1
    elif a1[i] >= a2[j]:
      joined.append(a2[j])
      j += 1

    if i == len(a1) and j == len(a2):
      return joined
    elif i == len(a1):
      return joined + a2[j:]
    elif j == len(a2):
      return joined + a1[i:]
  
@timeit
def merge_sorted_arrays3(a1: list, a2: list) -> list:

  joined = []
  a_item_1 = a1[0]
  a_item_2 = a2[0]

  i = 1
  j = 1

  while a_item_1 or a_item_2:

    if ((not a_item_2) or a_item_1 < a_item_2):
      joined.append(a_item_1)
      if i == len(a1):
        a_item_1 = None
      else:
        a_item_1 = a1[i]
        i += 1
    
    else:
      joined.append(a_item_2)
      if j == len(a2):
        a_item_2 = None
      else:
        a_item_2 = a2[j] if not None else None
        j += 1

  return joined
