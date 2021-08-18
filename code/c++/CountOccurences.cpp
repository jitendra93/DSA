#include <iostream>


template <class T>
int numberOfOccurences(T arr[], T target){
    int count = 0;
    int arrSize = *(&arr + 1) - arr;
   for (int i = 0; i < arrSize; i++)
   {
       if(arr[i]==target){
           count=count+1;
       }
   }
   return count;

}


int main(){
    int arr[] = {1, 2, 2, 2 , 6, 7, 8};
    int res = numberOfOccurences<int>(arr,2);
    std::cout << res;
}


