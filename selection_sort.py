#selection sort in increasing order
array = [5,6,7,1,2,78,32,62,12,8,2,7]

def selectionSort(arrayEx2) :
  for m in range(0, len(arrayEx2)) :
    maxElem = getMax(arrayEx2)
    key = arrayEx2[m]
    for j in range(m, len(arrayEx2)) :
      if(arrayEx2[j] >= maxElem) :
        maxElem = arrayEx2[j]
        k = j
    arrayEx2[k] = key
    arrayEx2[m] = maxElem
  return arrayEx2
  
res = selectionSort(array)
print(res)

#selection sort in decreasing order
array = [5,6,7,1,2,78,32,62,12,8,2,7]

def selectionSort(arrayEx1) :
  for m in range(0, len(arrayEx1)) :
    minElem = getMin(arrayEx1)
    key = arrayEx1[m]
    for j in range(m, len(arrayEx1)) :
      if(arrayEx1[j] <= minElem) :
        minElem = arrayEx1[j]
        k = j
    arrayEx1[k] = key
    arrayEx1[m] = minElem
  return arrayEx1
  
res = selectionSort(array)
print(res)

def getMax(array1) :
  for i in range(0, len(array1)) :
    if(array1[i] >= maxElem) :
        maxElem = array1[i]
  return maxElem

def getMin(array2) :
  for f in range(0, len(array2)) :
    if(array2[f] <= maxElem) :
        maxElem = array2[f]
  return maxElem
 
