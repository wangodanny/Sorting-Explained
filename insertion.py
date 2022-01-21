#Define the sorting function, which takes in the input from the user.
def insertion(nums):
  print("\nInsertion sort is a simple sorting algorithm that works similar to the way you sort playing cards in your hands. The array is virtually split into a sorted and an unsorted part. Values from the unsorted part are picked and placed at the correct position in the sorted part.\n")
  # Traverse through 1 to the end of the array
  for i in range(1, len(nums)):
 
    key = nums[i]
 
    # Move elements of nums[0..i-1], that are greater than key, to one position ahead of their current position
    j = i-1
    while j >= 0 and key < nums[j] :
      print("\n"+str(nums[j]) + " is bigger than "+ str(key) + " so it is being moved.")
      nums[j + 1] = nums[j]
      j -= 1
      nums[j + 1] = key
    print ("\nArray Pass:", i)
    print (nums)
    input("\nPress enter to continue\n")
  print("All done")
