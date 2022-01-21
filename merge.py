#Define the sorting function, which takes in the input from the user.
def mergeSort(nums):
  if len(nums) > 1:

    # Finding the mid of the array
    mid = len(nums)//2

    # Dividing the array elements
    L = nums[:mid]

    # into 2 halves
    R = nums[mid:]

    # Sorting the first half
    mergeSort(L)

    # Sorting the second half
    mergeSort(R)

    i = j = k = 0

    # Copy data to temp arrays L[] and R[]
    while i < len(L) and j < len(R):
      if L[i] < R[j]:
        nums[k] = L[i]
        i += 1
      else:
        nums[k] = R[j]
        j += 1
        k += 1
  
    # Checking if any element was left
    while i < len(L):
      nums[k] = L[i]
      i += 1
      k += 1

    while j < len(R):
      nums[k] = R[j]
      j += 1
      k += 1

  print(nums)

