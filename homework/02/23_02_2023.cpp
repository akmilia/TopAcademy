#include <iostream>

using namespace std;

void init(int *a, int size);
void out(int *a, int size);
void out_c(int *a, int size);

int main()
{
setlocale(LC_ALL, "Russian");
int digit;

const int size_a = 15;
int a[size_a];
int *pa;
pa = &a[0];
//^ первый массив с указателем
const int size_b = 15;
int b[size_b];
int *pb;
pb = &b[0];
//^ второй массив с указателем
const int size_c = size_a + size_b;
int c[size_c];
int *pc;
pc = &c[0];
//^ третий массив с указателем
int tmp = 0;
do
{
init(a, size_a);
out(a, size_a);

init(b, size_b);
out(b, size_b);

cout << "Эта программа создаёт третий массив, в котором собирает:\n";
cout << "1 - Элементы обоих массивов;\n";
cout << "2 - Общие элементы двух массивов;\n";
cout << "3 - Элементы массива A, которые не включаются в B;\n";
cout << "4 - Элементы массива B, которые не включаются в A;\n";
cout << "5 - Элементы массивов A и B, коотрые не являются общими для них(то есть объединение результатов двух предыдущих вариантов)\n\n";
cin >> digit;
switch (digit){
case 1:
for (pc = c, pa = a; pc < c + size_a + size_b; pc++, pa++)
*pc = *pa;
for (pc = c + size_a, pb = b; pc < c + size_a + size_b; pc++, pb++)
*pc = *pb;
cout << "\nРезультат:\n\n";
out(c, size_c);
break;
case 2:
pc = c;
for (pa = a; pa < a + size_a; pa++){
for (pb = b; pb <b + size_b; pb++){
if (*pa == *pb){
*pc = *pa;
pc++;
}
}
}
cout << "\nРезультат:\n\n";
out_c(c, size_c);
break;
case 3:
pc = c;
tmp = 0;
for (pa = a; pa < a + size_a; pa++){
for (pb = b; pb <b + size_b; pb++){
if (*pa == *pb)
tmp++;
}
if (tmp == 0){
*pc = *pa;
pc++;
}
tmp = 0;
}
cout << "\nРезультат:\n\n";
out_c(c, size_c);
break;
case 4:
pc = c;
tmp = 0;
for (pb = b; pb <b + size_b; pb++){
for (pa = a; pa < a + size_a; pa++){
if (*pb == *pa)
tmp++;
}
if (tmp == 0){
*pc = *pb;
pc++;
}
tmp = 0;
}
cout << "\nРезультат:\n\n";
out_c(c, size_c);
break;
case 5:
pc = c;
tmp = 0;
for (pa = a; pa < a + size_a; pa++){
for (pb = b; pb <b + size_b; pb++){
if (*pa == *pb)
tmp++;
}
if (tmp == 0){
*pc = *pa;
pc++;
}
tmp = 0;
}
for (pb = b; pb <b + size_b; pb++){
for (pa = a; pa < a + size_a; pa++){
if (*pb == *pa)
tmp++;
}
if (tmp == 0){
*pc = *pb;
pc++;
}
tmp = 0;
}
cout << "\nРезультат:\n\n";
out_c(c, size_c);
break;
}
cout << "\nЕсли хотите продолжить, нажмите 1:";
cin >> digit;
} while (digit == 1);
}

void init(int *a, int size)
{
srand(time(NULL));
for (int i = 0; i < size; a++, i++)
*a = rand() % 20 + 1;
}

void out(int *a, int size)
{
cout << "\n";
for (int i = 0; i < size; a++, i++)
cout << *a << " ";
cout << "\n";
}

void out_c(int *a, int size)
{
cout << "\n";
for (int i = 0; i < size; a++, i++)
if (*a>0) cout << *a << " ";
cout << "\n";
}
