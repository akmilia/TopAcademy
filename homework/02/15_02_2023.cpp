#include <iostream>
#include <stdio.h>
#include <cstring>
#include <cctype>
using namespace std;
 
class String
{
protected:
    char *p;   //сохраняет адрес динамически выделяемой памяти для размещения символов строки;
    int length;   //сохраняет длину строки в байтах;
public:
    String();   //конструктор без параметров;
    String(const char *str);   //конструктор, принимающий в качестве параметра строку, заканчивается нулевым байтом
    String(char c);   //конструктор, принимающий в качестве параметра символ char;
    String(const String &obj);   //конструктор копирования;
    ~String();   //Деструктор
};
 
String::String()
{
    :s(0),n(0){};  //как можно реализовать конструктор без параметров?
}
 
String::String(const char *str)
{
    n = strlen(str);   // strlen должна видеть начало Си-строки
    s = new char[n+1];  
    strcpy(s, str);   //копирует строки s, str
}
 
String::String(char c);
{
    s = new char[2];
    s[0] = c;
    s[1] = '\0';
    n=1;
} 
 
String::String(const String &obj)
{
    n = obj.n;
    s = new char[n+1];
    strcpy(s, obj.s);
}
 
String::~String()
{
    delete [] s;   //Деструктор
}
 
class IdentifierString : public String  
{
public:
  IdentifierString(const char* str) : String(str) {}
};