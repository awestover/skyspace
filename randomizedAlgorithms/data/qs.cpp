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
  return low;
}

// Note: I assume that the elements of A are all distinct in this simplisitc implementation of quicksort, it is easy to modify this code to work for arrays that can have duplicate elements 
void quicksort(int* A, int n){
  if(n>1){
    int pivot = A[rand()%n]; // randomly select the pivot
    int splitIndex = partition(A, n, pivot);
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
}
