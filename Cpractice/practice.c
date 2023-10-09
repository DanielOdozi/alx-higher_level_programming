#include <stdio.h>

int add(int a, int b)
{
    int add;
    add = a + b;
    return (add);
}

int main(){
    int a;
    int b;
    int c;
    char mystring[] = "\"Programming is like building a multilingual puzzle";
    char newstring[] = "with proper grammar, but the outcome is a piece of art,";

    a = 100;
    b = 105;
    c = add(a, b);

    printf("%d\n", c);
    puts(mystring);
    printf("%s\n", newstring);
    return 0;
}