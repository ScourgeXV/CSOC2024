'''Quick Sort algorithm '''


def partition(array, left_idx,right_idx):
    pivot = array[right_idx]
    i = left_idx - 1

    for j in range(left_idx,right_idx):
        if array[j] <= pivot:
            i += 1
            array[i],array[j] = array[j],array[i]

    array[i + 1],array[right_idx] = array[right_idx],array[i + 1]
    return i + 1


def quick_sort(array,left_idx,right_idx):
    if left_idx < right_idx:
        p = partition(array,left_idx,right_idx)
        quick_sort(array,left_idx, p - 1)
        quick_sort(array,p + 1,right_idx)
