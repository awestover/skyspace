#include <iostream> 

int main() {

    int* arr = (int*)malloc(sizeof(int)*10);
    for (int i = 0; i < 10; ++i) {
        arr[i] = i*i;
        std::cout << arr+i << std::endl;
    }
    
    std::cout << arr << std::endl;
    std::cout << arr[1] << std::endl;
    std::cout << (arr+1)[0] << std::endl;

    bool* arrB = (bool*)malloc(sizeof(int)*10);
    for (int i = 0; i < 10; ++i) {
        std::cout << arrB+i << std::endl;
    }
    
    return 0;
}
