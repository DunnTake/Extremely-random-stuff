#include <stdio.h>
#include <math.h>

int main()
{
    int a;
    printf("Enter an integer to test prime: ");
    scanf("%i",&a);
    int lim = (int)sqrt(a);

    //Default primes
    if (a == 2 || a == 3 || a == 5) {printf("%i is not prime\n", a); return 0;}
    //Default not primes
    if (a % lim == 0 || a % 2 == 0 || a % 3 == 0 || a == 1) {printf("%i is not prime\n", a); return 0;}
    
    int k = 1;
    while (1)
    {
        if (6*k-1 > lim) {break;}
        if (a % (6*k-1) == 0) {printf("%i is not prime\n", a); return 0;}
        if (6*k+1 > lim) {break;}
        if (a % (6*k+1) == 0) {printf("%i is not prime\n", a); return 0;}
        k++;
    }
    printf("%i is prime\n", a);
    return 0;
}