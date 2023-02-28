#include <iostream>
class Drop {
    int a,b; // ( a / b )

    public:
    Drop(){};
    Drop(const Drop &other):Drop(other.a,other.b){};
    Drop(int a, int b){
        this-> a=a;
        this->b=b;
    }

    void print(){
        std::cout << "this is "<<this->a <<"/"<<this->b<<"\n";
    }

    void input(){
        std::cout << "input a: ";
        std::cin >> this->a;
        std::cout << "input a: ";
        std::cin >> this->b;
    }

    void plus(int val){
        val = val * this->b;

        this->a=this->a+val;
    }

    void minus(int val){
        plus(-val);
    }
    

    ~Drop() {}
};

int main(int arqc, char const *arqv[])
{
    Drop test;

    test.input();

    test.print();

    test.plus(4);

    test.print();
    return 0;
}