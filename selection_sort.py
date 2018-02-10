#selection sort in increasing order
array = [5,6,7,1,2,78,32,62,12,8,2,7]

def selectionSort(arrayEx) :
  for m in range(0, len(arrayEx)) :
    maxElem = 0
    key = arrayEx[m]
    for j in range(m, len(arrayEx)) :
      if(arrayEx[j] >= maxElem) :
        maxElem = arrayEx[j]
        k = j
    arrayEx[k] = key
    arrayEx[m] = maxElem
  return arrayEx
  
res = selectionSort(array)
print(res)
