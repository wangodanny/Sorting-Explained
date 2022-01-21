#Define the bubble sorting function, which takes in the input from the user.
def bubble(nums):
  print("\nBubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order.\n")
  print("Starting array: "+str(nums)+"\n")
  n = len(nums)
  
# Swap the elements to arrange in ascending order
# Traverse through all array elements
  for i in range (len(nums)):
    print("Array pass:"+str(i)+"\n")
    # Last elements in the array are already in place so don't count them
    for j in range(0, n-i-1):
      print("Swap pass:", j+1)
      # Traverse the array from 0 to the last sorted element (the for loop above)
      # Swap if the element found is greater than the next element (thanks selection sort for a swapping method that does not need temp values)
      if nums[j] > nums[j+1]:
        print(str(nums[j])+" is bigger than "+ str(nums[j+1]) + " so it is being swapped.")
        nums[j], nums[j+1] = nums[j+1], nums[j]
        print(str(nums)+"\n")
      else:
        print("No swaps required.\n")
    print(nums)
    input("Press enter to continue\n")
  print("All done")