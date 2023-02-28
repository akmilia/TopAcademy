#include <iostream>
#include <ctime>
int main(){  
    srand(time(NULL));
    int size,size2;
    std::cout<<"Введите размер чисел: ";
    std::cin>>size>>size2;
    int mini, maxi;   
    std::cout<<"Введите минимальное и максимальное число: ";
    std::cin>>mini>>maxi;
    int sum=0;
    int** arr=new int* [size];
    for(int i=0;i<size;++i){
        arr[i]=new int[size2];
        for(int j=0;j<size2;++j){
            arr[i][j] = rand()%(maxi-mini+1)+mini;
            std::cout<<arr[i][j] <<"\t";
            sum +=arr[i][j];
        }
        std::cout<<"\n";
    }
    std::cout<<"Среднее: "<< (double)sum/(size*size2)<<"\t";
    return 0;
}