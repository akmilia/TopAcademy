#include <iostream>

bool isPrime(int num){
    for(int i=2;i<num;++i){
            if(num%i==0){
            return false;
    }
    return true;
}
int main(){
    std::cout<<"Первое число: ";
    int a;
    std::cin>>a;
    std::cout<<"\n";
    std::cout<<"Второе число: ";
    int b;
    std::cin>>b;
       std::cout<<"\n";
    int k=0;
    while(a<=b){
        for(int i=a;i<=b;++i){
            if(isPrime(i)==true){
                cout
            }
        }
    }
    std::cout<< b<<"\n";
    std::cout<<"Количество этих чисел: "<<k;
}
