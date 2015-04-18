def BubbleSort(a):
  for i in range(len(a)):
    print i
    for j in range(len(a) - i - 1):
      if a[j] > a[j+1]:
        temp = a[j]
        a[j] = a[j+1]
        a[j+1] = temp
  return a

if __name__ == "__main__":
  a = [54,26,93,17,77,31,44,55,20]
  BubbleSort(a)
  print a
