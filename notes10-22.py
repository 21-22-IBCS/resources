import time
import random

def mergeSort(li2):
    if len(li2) > 1:
        m = len(li2)//2
        left = li2[:m]
        right = li2[m:]
        mergeSort(left)
        mergeSort(right)
        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                li2[k] = left[i]
                i += 1
            else:
                li2[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            li2[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            li2[k] = right[j]
            j += 1
            k += 1

def selectionSort(li):
    sortedList = []
    while len(li) > 0:
        minE = li[0]
        for i in range(len(li)):
            if li[i] < minE:
                minE = li[i]
        li.pop(li.index(minE))
        sortedList.append(minE)

    return sortedList


def main():

    n = 500
    
    listOfDifferences = []
    for i in range(10):

        test1 = []
        for i in range(n):
            test1.append(random.randint(1,n))
        
        start = time.time()
        selectionSort(test1)
        stop = time.time()
        difference = stop - start
        listOfDifferences.append(difference)
   
    total = 0
    for dif in listOfDifferences:
        total = total + dif
    avgTime = total/10
    print("\nThe average time to sort this list was " + str(avgTime) + " seconds.")

if __name__ == "__main__":
    main()
