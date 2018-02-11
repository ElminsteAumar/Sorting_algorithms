def merge(L, R):
  array = []
  i, j = 0, 0
  while i < len(L) and j < len(R):
    if L[i] <= R[j]:
      array.append(L[i])
      i += 1
    else:
      array.append(R[j])
      j += 1
  array += L[i:]
  array += R[j:]
  return array

def mergesort(array):
  if len(array) > 1:
    q = len(array) // 2
    L = mergesort(array[:q])
    R = mergesort(array[q:])
    return merge(L, R)
  return array
  
arrayEx = [12,64,23,58,34,72,12,7,29]
res = mergesort(arrayEx)
print(res)
