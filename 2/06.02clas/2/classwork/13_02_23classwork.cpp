#include <iostream>
#include <string>

template <typename T>
class Array{
    private:
        int size;
        int cap;
        T *arr;
    
    public:
        Array(const Array &other) : Array(other.arr,other.size){};

        Array(){}
        
        Array(int  size, T val, int cap){
            this-> arr = new T[size];
            this-> size = size;
            this-> cap = cap;
            for(int i=0; i < size; ++i){
                this-> arr[i]=val;
            }
        }

    void recap(int cap){
        this-> cap = cap;
    }

    void add_back(int val){
        if(this->size + 1 > this->cap){
             std::cout <<"No cap = "<<this->cap<<"\n";
    }
    else{
        this-> arr[size] = val;
        size +=1;
        }
    }


    void add_end(const T &val){
        if(this->cap < this-> size +1){
            recap(size*2);
        }
        this->arr[this->size] = val;
        this->size++;
    }

    void add_begin(const T &val){
        if(this->cap < this->size +1){
            recap(size*2);
        }
        this->size++;
        for(int i=0; i < size;++i){
            this->arr[0] = val;
        }
    }

    void dobavvper(const T&val){
        if(this->cap < this->size+1){
            recap(size*2);
        }
        for (int i=size; i >=0;--i){
            arr[i]=arr[i-1];
        }
        arr[0]=val;
        this->size++;
    }
    void dobav(int i, int val){

        add_back(val);
}
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

    void printarr() {
        std::cout<< "[";
        for(int i=0;i<this->size;++i){
            std::cout << this->arr[i] << ", ";
        }
            std::cout << "]\n";
        }

    void delete_end(const T&val){
        this->size--;
    }

    T &operator[](int i){
        return arr[i];

    }

    ~Array(){
        delete [] this->arr;
    }
};

//template <typename T>
//void print_arr(Array &arr)
//for (int i=0; i<arr.getSize();++i){
//   std::cout <<arr[i]<<
//}


class Algoritm{
    private:
        int size2;
        int cap2;
        T *arr2;
    
    public:
        Algoritm(const Array &other) : Algoritm(other.arr2,other.size2){};

        Algoritm(){}
        
        Algoritm(int  size, T val, int cap2){
            this-> arr2 = new T[size2];
            this-> size2 = size2;
            this-> cap2 = cap2;
            for(int i=0; i < size2; ++i){
                this-> arr2[i]=val;
            }
        }

    void recap(int cap2){
        this-> cap2 = cap2;
    }

    void add_back(int val){
        if(this->size2 + 1 > this->cap2){
             std::cout <<"No cap = "<<this->cap2<<"\n";
    }
    else{
        this-> arr[size2] = val;
        size +=1;
        }
    }

    void printarr() {
        std::cout<< "[";
        for(int i=0;i<this->size2;++i){
            std::cout << this->arr2[i] << ", ";
        }
            std::cout << "]\n";
        }

};
int main(){
Array<int> arr(5, 1, 6);
arr.printarr();
arr.dobav(0,2);
arr.printarr();
arr.dobavvper(2);
arr.printarr();
arr.erase(0);
arr.printarr();
arr.erase(5);
arr.printarr();
arr[0];
Algoritm<int> arr(5, 6, 6);
arr.printarr();

return 0;
}
