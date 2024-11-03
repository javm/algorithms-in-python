def mean(data):
  sum = 0
  for i in range(len(data)):
    sum += data[i]
  return sum / len(data)

def median(data):
  n = len(data)
  data.sort()
  if n % 2 == 0:
    return (data[n//2 - 1] + data[n//2]) / 2
  else:
    return data[n//2]
  
print(mean([1, 2, 3, 4, 5])) # 3.0
print(median([12, 13, 6, 7, 19])) # 12