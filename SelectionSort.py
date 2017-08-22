# function to find the smallest number
def findSmallest(arry):
    smallest = arry[0];
    smallest_index = 0;
    for i in range(1, len(arry)):
        if arry[i] < smallest:
            smallest = arry[i];
            smallest_index = i;
    return smallest_index;


# function to find the greatest number
def findGreatest(arry):
    greatest = arry[0];
    greatest_index = 0;
    for i in range(1, len(arry)):
        if arry[i] > greatest:
            greatest = arry[i];
            greatest_index = i;
    return greatest_index;


# Sorting the array in selection sort
def selectionSort(arr):
    newArray = []
    for i in range(len(arr)):
        smallest = findGreatest(arr)  # will return the index of the item in the array
        newArray.append(arr.pop(smallest))
    return newArray


print selectionSort([300, 5, 20, 220, 3, 6, 300, 2, 10, 100]);


# function to find the duplicated array item
def findDuplicate(arry):
    duplicateFreeArray = []
    duplicatedArray = selectionSort(arry);
    dupNum = len(duplicatedArray);
    for i in range(dupNum):
        for j in range(i + 1, dupNum):
            if duplicatedArray[i] == duplicatedArray[j]:
                duplicateFreeArray.append(duplicatedArray[i])
    return duplicateFreeArray


print findDuplicate([300, 5, 20, 220, 3, 6, 300, 2, 10, 100, 2])
