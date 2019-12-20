#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int partition(int* A, int n, int pivot){
  int low = 0; int high = n-1;
  while (low < high){
    while(A[low] <= pivot && low < high){
      low++;
    }
    while(A[high] > pivot && low < high){
      high--;
    }
    int tmp = A[low];
    A[low] = A[high];
    A[high] = tmp;
  }
  if(A[low] <= pivot && low < n){
    low++;
  }
  for (int i = 0; i < low; ++i) {
    if (A[i] > pivot)
        printf("NOOOOOOOOOO @23");
  }
  for (int i = low; i < n; ++i) {
    if (A[i] <= pivot)
        printf("NOOOOOOOOOO @27");
  }
  return low;
}

// Note: I assume that the elements of A are all distinct in this simplisitc implementation of quicksort, it is easy to modify this code to work for arrays that can have duplicate elements 
void quicksort(int* A, int n){
  if(n>2){
    int pivot = A[rand()%n]; // randomly select the pivot
    int splitIndex = partition(A, n, pivot);
    printf("splitIndex: %d\n",splitIndex);
    quicksort(A, splitIndex);
    quicksort(A+splitIndex, n-splitIndex);
  }
}

int main(){
    srand(time(NULL)); // set seed for rng
    int n = 100;
    int* A = (int*)malloc(sizeof(int)*n);
    for (int i = 0; i < n; ++i) {
        A[i] = rand();
    }
    quicksort(A, n);
    for (int i = 0; i < n; ++i) {
        for (int j = i+1; j < n; ++j) {
            if (A[i] > A[j])
                printf("A[%d] > A[%d]\n", i, j);
        }
    }
}
