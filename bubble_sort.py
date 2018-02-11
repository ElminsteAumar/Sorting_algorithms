
def bubbleSort(array) :
  for m in range(0, len(array)) :
    for i in range(1, len(array) - m) :
      if array[i-1] > array[i] :
        array[i-1], array[i] = array[i], array[i-1]
  return array
  
arrayEx = [12,125,122,1200,4,143]
res = bubbleSort(arrayEx)
print(res)
