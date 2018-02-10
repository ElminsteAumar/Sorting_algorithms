#selection sort in increasing order
array = [5,6,7,1,2,78,32,62,12,8,2,7]

def selectionSort(arrayEx) :
  for m in range(0, len(arrayEx)) :
    maxElem = -float('inf')
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


#selection sort in decreasing order
array = [5,6,7,1,2,78,32,62,12,8,2,7]

def selectionSortReverse(arrayEx1) :
  for m in range(0, len(arrayEx1)) :
    minElem = float('inf')
    key = arrayEx1[m]
    for j in range(m, len(arrayEx1)) :
      if(arrayEx1[j] <= minElem) :
        minElem = arrayEx1[j]
        k = j
    arrayEx1[k] = key
    arrayEx1[m] = minElem
  return arrayEx1
  
res1 = selectionSortReverse(array)
print(res1)
 
