#Explain the algorithm to the user
def quickSortExplain(start, end, nums):
  print("\nQuickSort is a Divide and Conquer algorithm. It picks an element as pivot and partitions the given array around the picked pivot.\n")

  print("The starting array is: "+str(nums)+"\n")
  def partition(start, end, nums):
    '''' This function handles sorting part of quick sort. start points to the first element while end point to the last element of an array.'''

	  # Initializing pivot's index to start
    pivot_index = start
    pivot = nums[pivot_index]
    print("The current pivot is: "+ str(pivot))
    print ("The array currently looks like this: "+str(nums)+"\n")
    input("Press enter to continue\n")
	
	  # This loop runs till start pointer crosses end pointer, and when it does we swap the pivot with element on end pointer
    while start < end:
		# Increment the start pointer till it finds an element greater than pivot
      while start < len(nums) and nums[start] <= pivot:
        start += 1
			
		  # Decrement the end pointer till it finds an element less than pivot
      while nums[end] > pivot:
        end -= 1
		
		  # If start and end have not crossed each other, swap the numbers on start and end
      if(start < end):
        nums[start], nums[end] = nums[end], nums[start]
	
	  # Swap pivot element with element on end pointer.
	  # This puts pivot on its correct sorted place.
    
    nums[end], nums[pivot_index] = nums[pivot_index], nums[end]
	
	  # Returning end pointer to divide the array into 2
    return end
	
  # The main function that implements QuickSort, which takes in the input from the user.
  def quicksort(start, end, nums):
    if (start < end):
      #print (nums,"\n")
		  # p is partitioning index, nums[p] is at right place
      p = partition(start, end, nums)
		
		  # Sort elements before partition and after partition
      quicksort(start, p - 1, nums)
      quicksort(p + 1, end, nums)
  
  quicksort(start, end, nums)
  print("All done!")