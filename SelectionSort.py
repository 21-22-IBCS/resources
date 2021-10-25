import time
import random

'''def mergeSort(li2):
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
            k += 1'''

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
    l1 = []
    l2 = []
    n = 100
    for i in range(n):
        l1.append(random.randint(1,n))
        l2.append(random.randint(1,n))
        
    start = time.time()
    result = selectionSort(l1)
    stop = time.time()

    totalSTime = stop - start
    print(result)
    print("")
    

    start = time.time()
    mergeSort(l2)
    stop = time.time()

    totalMTime = stop - start
    print(l2)
    print("")
    print("The Selection Sort for " + str(n) + " elements took " + str(totalSTime) + " seconds.")
    print("")
    print("The Merge Sort for " + str(n) + " elements took " + str(totalMTime) + " seconds.")
    
if __name__ == "__main__":
    main()
