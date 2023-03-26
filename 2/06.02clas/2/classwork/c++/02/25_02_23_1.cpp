#include <iostream>
#include <string>

class Student {
    protected:
    std::string name;
    int age;
    int rost;

    public: 

    Student() {}
};

class prepod : public Student {
    int work_mark;

    public:

    prepod() : prepod("none", 0, 0) {}

    prepod(std::string name, int age, int rost) {
        this->name = name;
        this->age = age;
        this->rost = rost;
    }

    std::string get_info() {
        std::string res = "";
        res += this->name + " " + std::to_string(this->age) + " " + std::to_string(this->rost);

        return res;
    }
};

std::ostream &operator<<(std::ostream &out, prepod &prepod) {
    out << prepod.get_info();

    return out;
}

int main() {

    prepod prepod("Никита", 16, 193);

    std::cout << prepod;

    return 0;
}