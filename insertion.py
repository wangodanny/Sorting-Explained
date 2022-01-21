#Define the sorting function, which takes in the input from the user.
def insertion(nums):
 
  # Traverse through 1 to the end of the array
  for i in range(1, len(nums)):
 
      key = nums[i]
 
      # Move elements of arr[0..i-1], that are
      # greater than key, to one position ahead
      # of their current position
      j = i-1
      while j >= 0 and key < nums[j] :
        nums[j + 1] = nums[j]
        j -= 1
        nums[j + 1] = key
  print (nums)

  #Add iteration passes!