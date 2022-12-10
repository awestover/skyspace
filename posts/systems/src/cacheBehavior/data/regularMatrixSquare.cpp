#include <cstdlib>
#include <ctime>

int main(){
    srand(time(NULL)); // random seed
    
    // randomly initiallize the array A
    int N = 1<<10;
    int* A = (int*)malloc(sizeof(int)*N*N);
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            A[i*N+j] =  rand()%1000;
        }
    }

    // allocate room to store the product
    int* A_squared = (int*)malloc(sizeof(int)*N*N);

    // square A
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            int sum = 0;
            for (int k = 0; k < N; ++k) {
                sum += A[i*N+k] * A[k*N+j];
            }
            A_squared[i*N+j] = sum;
        }
    }

    return 0;
}
