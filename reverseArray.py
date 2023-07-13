lst = list(map(int, input().split()))
def reverse_Array(lst):
  i = 0
  j = len(lst) - 1
  while(i <= j):
        temp = lst[i]
        lst[i] = lst[j]
        lst[j] = temp
        i += 1
        j -= 1
  return lst
print(reverse_Array([1, 2, 3, 4]))
print(reverse_Array([2, 5, 6]))
print(reverse_Array([1, 1, 10]))
print(reverse_Array(lst))

    
