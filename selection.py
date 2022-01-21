#Define the sorting function, which takes in the input from the user.
def selection(nums):
  print("Selection Sort test")
  
  #For the length of the entire array set the minumum to the next unsorted item in the array
  for index in range(len(nums)):
      min_index = index
      #For the length of the array starting from the current index value (array item number), compare the current number to the smallest number in the sorted array
      for j in range( index +1, len(nums)):
        #If the new number is smaller than the current number in sorted array then swap them
         if nums[min_index] > nums[j]:
          min_index = j

# Swap the minimum value with the compared value
      nums[index], nums[min_index] = nums[min_index], nums[index]

  print(nums)