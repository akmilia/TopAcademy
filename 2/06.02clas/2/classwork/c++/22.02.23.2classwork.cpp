#include <iostream>
#include <memory>


template <typename T>
class Array {
    std::unique_ptr<T []> array;
    int size;
    int cap;

    public:
    Array() : Array(4,4) {}
    Array(const Array &other) {}
    Array(int size, T val) : array(new T[size]){ // как пример конструктор от размера и знчения (необязтельно)
    this->size=size;

    for(int i=0; i<size; ++i){
        this->array.get()[i]=val;
    }
    }


    void recap(int cap){
        this-> cap = cap;
    }

   void add_begin(const T &val){
    for(int i=size;i>0;i--){
        if(this->cap < this->size +1){
            recap(size*2);
        }
        this->size++;
        this->array[0] = val;
        }
   }
    void add_end(T val) {} // добавить в конец

    void del_begin() {} // удалить из начала
    void del_end() {} // удалить из конца


    void print() const {
    std::cout<< "[";
    for(int i=0;i<this->size;++i){
        std::cout << array.get()[i] << ", ";
    }
    std::cout << "]\n";
}

    ~Array() {}
};

int main(){

    Array<int> array(4,4);
    array.print();
    array.add_begin(5);
    array.print();
    return 0;
}