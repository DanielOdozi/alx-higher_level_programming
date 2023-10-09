#include <stdlib.h>
#include <time.h>
#include <stdio.h>
/* more headers goes there */

/* betty style doc for function main goes there */
int main(void)
{
	int n;
    int a;
    char alp = 'A';
    int i;
    
	srand(time(0));
	n = rand() - RAND_MAX / 2;

    a = n % 10;
	if (a > 5)
	{
		printf("Last digit of %d is %d and is greater than 5\n", n, a);
	}
	else if (a < 6 && a != 0)
	{
		printf("Last digit of %d is %d and is less than 6 and not 0\n", n, a);
	}
	else if (a == 0)
	{
		printf("Last digit of %d is %d and is 0\n", n, a);
	}


	while (alp <= 'Z')
	{
		putchar(alp);
		alp++;
	}
	putchar('\n');

	for (i = 0; i < 10; i++)
	{
		printf("%d", i);
	}
    printf("\n");
	return (0);
}