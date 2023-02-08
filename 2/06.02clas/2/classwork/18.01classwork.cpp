#include <iostream>

class Array {
    int *arr;
    int size; //сколько в массиве элементов
    int cap; //вместимость массива максимальная

public:
explicit Array(int cap){
    this->arr = new int[cap];
    this->cap = cap;
    size = 0;
}

//если ошибка
void add_back(int val){
    if (this->size + 1 >= this->cap){
        std::cout <<"No cap = "<<this->cap<<"\n";
    }
    else{
        this-> arr[size] = val;
        size +=1;
    }
}
//вывод в консоль
void print() const {
    std::cout<< "[";
    for(int i=0;i<this->size;++i){
        std::cout << this->arr[i] << ", ";
    }
    std::cout << "]\n";
}



~Array(){
        delete [] this->arr;
    }
    //замена символа на другой
void insert(int i, int val){
    if(i<0||i>=this->size){
        std::cout<<"error\n";
    }
    else{
        this->arr[i]=val;
    }
}
//удаление элемента
void erase(int index){
      if(index<0||index>=this->size){
        std::cout<<"error\n";
    }
    else{
    for (int i = index+1; i < this-> size;++i){
        this->arr[i-1]=this->arr[i];
    }
    this-> size-=1;
}
}
//добавляем число
Array &operator+(int val){
    add_back(val);
    return *this;
}
//удаляем число
Array &operator-(int val){
    for(int i=0;i< this->size;++i){
        if(arr[i]==val){
            erase(i);
        }
    }
    return *this;;
}

bool operator<(Array other){
    return this->size < other.size;
}


};


int main(){
    Array arr(15);

    arr.add_back(1);
    arr.add_back(2);
    arr.add_back(3);
    arr.add_back(4);
    arr.print();
    arr.add_back(5);
    arr.add_back(6);
    arr.print();


    arr.insert(1,22);
    arr.print();
    arr.erase(1);
    arr.print();

    arr + 6;
    arr.print();

    arr - 3;
    arr.print();

    return 0;
}
