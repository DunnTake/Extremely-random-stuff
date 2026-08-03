#include <stdio.h>
#include <math.h>
#include <stdint.h>
#include <time.h>

int elapsed(clock_t t0)
{
    clock_t t1 = clock();
    double delta = (double)(t1 - t0) / CLOCKS_PER_SEC;
    printf("Runtime: %f seconds\n", delta);
}

int main()
{

    int64_t a;
    printf("Enter an integer to test prime: ");
    scanf("%lld",&a);
    if (a < 0) {printf("Invalid, int must be positive"); return 0;};
    int64_t lim = (int64_t)sqrt(a);

    //Default primes
    if (a == 2 || a == 3 || a == 5) {printf("%lld is not prime\n", a); return 0;}
    //Default not primes
    if (a % 2 == 0 || a % 3 == 0 || a == 1 || a % lim == 0) {printf("%lld is not prime\n", a); return 0;}
    
    clock_t t0 = clock();
    int64_t k = 1;
    for (;;) {
        if (6*k-1 > lim) {break;}
        if (a % (6*k-1) == 0) {
            printf("%lld is not prime\n", a);
            elapsed(t0);
            return 0;
        }
        if (6*k+1 > lim) {break;}
        if (a % (6*k+1) == 0) {
            printf("%lld is not prime\n", a);
            elapsed(t0);
            return 0;
        }
        k++;
    }
    printf("%lld is prime\n", a);
    elapsed(t0);
    return 0;
}