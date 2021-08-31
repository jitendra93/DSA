#include <iostream>

template <class T>
void fill(T* arr, int start , int end, const T& val){
    for (int i = start; i < end; i++)
    {   
        arr[i] = val;
    }
}

int main(){
    int arr[] = {1, 2, 2, 2 , 6, 7, 8};

    fill<int>(arr,0,7,100);

    for (int i = 0; i < 7; i++)
    {
        std::cout << arr[i];
        std::cout << "\n";
    }
    

}