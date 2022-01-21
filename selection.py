#Define the sorting function, which takes in the input from the user.
def selection(nums):
  print("\nThe selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) from unsorted part and putting it at the beginning.\n")
  
  #For the length of the entire array set the minumum to the next unsorted item in the array
  for index in range(len(nums)):
    min_index = index
    #For the length of the array starting from the current index value (array item number), compare the current number to the smallest number in the sorted array
    for j in range( index +1, len(nums)):
      #If the new number is smaller than the current number in sorted array then swap them
      if nums[min_index] > nums[j]:
        print("\n"+str(nums[j])+" is smaller than "+str(nums[min_index])+ " so it is being moved to the start.\n")
        min_index = j
        #Swap the minimum value with the compared value then output
        nums[index], nums[min_index] = nums[min_index], nums[index]
        print(nums)
      else:
        print("\nNo changes here.\n")
        print(nums)
      input("Press enter to continue\n")

  print("\nAll done!")