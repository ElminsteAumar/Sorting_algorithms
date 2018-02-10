#insertion sort
array = [4,1,6,3,2,5,7]

def insertionSort(arrayEx) :
  for j in range(1, len(arrayEx)) :
    key = arrayEx[j]
    i = j - 1
    while i >= 0 and arrayEx[i] > key :
      arrayEx[i + 1] = arrayEx[i]
      i = i - 1
    arrayEx[i + 1] = key
  return arrayEx
  
res = insertionSort(array)
print(array)

# reverse insertion sort
def insertionSortReverse(arrayExReverse) :
  for m in range(1, len(arrayExReverse)) :
    keyReverse = arrayExReverse[m]
    i = m - 1
    while i >= 0 and arrayExReverse[i] < keyReverse :
      arrayExReverse[i + 1] = arrayExReverse[i]
      i = i - 1
    arrayExReverse[i + 1] = keyReverse
  return arrayExReverse
  
resReverse = insertionSortReverse(array)
print(resReverse)
