#include <iostream>

int main(){
    //длина и ширина
    const int x = 21;
    const int y = 15;

    for(int i=0, i < y,++i){
        for(int j=0, j< x,++j){
            std::cout<<"*";
        }
        std::cout<<"\n";
    }

    return 0;
}