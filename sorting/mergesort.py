def mergesort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    return merge(left, right)
  
def merge(left, right):
  result = []
  while(left and right):
    if left[0] < right[0]:
      result.append(left.pop(0))
    else:
      result.append(right.pop(0))
  if left:
    result += left
  else:
    result += right
  return result

a = [3, 2, 1, 5, 4]
print(mergesort(a))  # [1, 2, 3, 4, 5]

b = [3, 2, 1, 5, 4, 6]
print(mergesort(b))  # [1, 2, 3, 4, 5, 6]