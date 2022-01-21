#Define the bubble sorting function, which takes in the input from the user.
def bubble(nums):
  print("Bubble Sort test")
  n = len(nums)

# Swap the elements to arrange in ascending order
# Traverse through all array elements
  for i in range (len(nums)):
  
      # Last elements in the array are already in place so don't count them
      for j in range(0, n-i-1):
  
          # Traverse the array from 0 to the last sorted element (the for loop above)
          # Swap if the element found is greater than the next element (thanks selection sort for a swapping method that does not need temp values)
          if nums[j] > nums[j+1]:
              nums[j], nums[j+1] = nums[j+1], nums[j]
      print("Array pass:", i)
      print(nums)