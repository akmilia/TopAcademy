#include <string>
#include <iostream>

class Calc {
private:
int a, b;

public:
    virtual void plus(double a, double b) {
        std::cout<<"Sum = "<<a + b<<"\n";
    }

    virtual void minus(double a,double b) {
        std::cout<<"minus = "<<a - b<<"\n";
    }

    ~Calc () {
        std::cout<<"Calc is gone\n";
    }

};

class SuperCalc : public Calc {

 public:
    void mult(double a, double b) { 
        std::cout<<"mult = "<<a * b<<"\n";
    }

    void div(double a, double b) { 
        std::cout<<"div = "<<a / b<<"\n";
    }

};

class SaveCalc : public Calc { 

    private:
    std::string last_operation; 

    public:
    std::string getLastOperation() {
        return this->last_operation;
    }

    void plus(int a, int b){
        std::string str = std::to_string(a) + "+" + std::to_string(b) + "=" + std::to_string(a+b);
        this->last_operation = str;

    }
    void minus(int a, int b){
        std::string str = std::to_string(a) + "-" + std::to_string(b) + "=" + std::to_string(a-b);
        this->last_operation = str;
      }


};

int main() {
    Calc def_calc;
    SuperCalc super_calc;
    SaveCalc save_calc;

    def_calc.minus(100, 50);
    def_calc.plus(5, 7);

    super_calc.minus(10, 8);
    super_calc.minus(50, 10);
    super_calc.mult(7, 11);
    super_calc.div(512, 16);

    save_calc.minus(77, 8);
    save_calc.plus(8, 60);
    std::cout << save_calc.getLastOperation() << "\n";

}