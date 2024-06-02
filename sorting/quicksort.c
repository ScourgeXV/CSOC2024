#include <stdio.h>

void swap(int *a, int *b) {
  int t = *a;
  *a = *b;
  *b = t;
}

int partition(int array[], int left_idx, int right_idx) {
  
  int pivot = array[right_idx];
  int i = (left_idx - 1);

  for (int j = left_idx; j < right_idx; j++) {
    if (array[j] <= pivot) {
      i++;
      swap(&array[i], &array[j]);
    }
  }

  swap(&array[i + 1], &array[right_idx]);
  return (i + 1);
}

void quick_sort(int array[], int left_idx, int right_idx) {
  if (left_idx < right_idx) {
    int p = partition(array, left_idx, right_idx);
    quick_sort(array, left_idx, p - 1);
    quick_sort(array, p + 1, right_idx);
  }
}
