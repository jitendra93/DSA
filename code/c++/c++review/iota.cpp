#include <iostream>
using namespace std;

template <class T>
void iota(T* a ,  int length ){
    for (int i = 0; i < length; i++)
    {
        a[i] = a[i] + 1;
    }
    
}

int main(){
     int arr[] = {1, 2, 2, 2 , 6, 7, 8};

    iota<int>(arr,7);

    for (int i = 0; i < 7; i++)
    {
        std::cout << arr[i];
        std::cout << "\n";
    }
    
}