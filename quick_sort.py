def quickSort(array, p, r) :
  if p < r :
    q = partition(array, p, r)
    quickSort(array, p, q - 1)
    quickSort(array, q + 1, r)
    return array

def partition(arrayEx, p, r):
  x = arrayEx[r]
  i = p - 1
  for j in range(p, r) :
    if arrayEx[j] <= x :
      i = i + 1
      arrayEx[i], arrayEx[j] = arrayEx[j], arrayEx[i]
  arrayEx[i + 1], arrayEx[r] = arrayEx[r], arrayEx[i + 1]
  return i + 1

arrayExample = [12,56,23,84,1200,64,23,75,35,109,98,117]
res = quickSort(arrayExample, 0, len(arrayExample)-1)
print(res)
