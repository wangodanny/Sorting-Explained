#Requirements:
# Quick, Selection, Bubble, Insertion, Merge - added
# Explain step by step - TBD
# Enable user to pick the algorithm - added
# Enable user input. - added

import random
import selection
import quicksort
import merge
import insertion
import bubble

# Generate an array of random numbers for later use in the algorithms.
def randomArray(arraySize):
  nums = []
  for x in range (arraySize):
    nums.append(random.randint(1, 22))
  selectSortChoice(nums)

# Send the array to the algorithm the user chose
def selectSortChoice (nums):
  print("Please enter the number of the algorithm you want to use (or exit): ")
  print("    1: Selection Sort")
  print("    2: QuickSort")
  print("    3: Merge Sort")
  print("    4: Insertion Sort")
  print("    5: Bubble Sort")
  print("    6: Exit")
  sortChoice = int(input("Enter your choice: "))

  if sortChoice == 1:
    selection.selection(nums)
  elif sortChoice == 2:
    # Also send the start and end posistions for partioning.
    quicksort.quicksort(0, len(nums) - 1, nums)
  elif sortChoice == 3:
    merge.mergeSort(nums)
  elif sortChoice == 4:
    insertion.insertion(nums)
  elif sortChoice == 5:
    bubble.bubble(nums)
  elif sortChoice == 6:
    exit()
  else:
    print("Sorry the option you selected is not valid. Please try again")
    selectSortChoice(nums)

print ("Hello and welcome to Sorting Explained, where we show step by step how the sorting algorithm you choose, works!\n")

arraySize = int(input("Please enter the number of items you want in your array: "))

randomArray(arraySize)

