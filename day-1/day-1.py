

def main():
    a = []
    b = []
    output = []

    f = open("advent-1-input.txt", "r")
    for x in f:
        line = x.split()
        a.append(int(line[0]))
        b.append(int(line[1]))

    quicksort(a)
    quicksort(b)
    for i in range(len(a)):
        if a[i] > b[i]:
            output.append(a[i] - b[i])
            continue
        output.append(b[i] - a[i])

    print(sum(output))

        



def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i+1], array[high] = array[high], array[i+1]
    return i+1

def quicksort(array, low=0, high=None):
    if high is None:
        high = len(array) - 1

    if low < high:
        pivot_index = partition(array, low, high)
        quicksort(array, low, pivot_index-1)
        quicksort(array, pivot_index+1, high)


main()
