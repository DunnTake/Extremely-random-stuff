// Bedao Mini Contest 21 - Bút chì
// https://oj.vnoi.info/problem/bedao_m21_a

#include <iostream>
using namespace std;

int main() {
    int T; //test_cases
    cin >> T ;
    
    if (T<1 || T>100) {
        cout << "Error: T out of range";
        exit(1);
    }

    for (int i = 1; i <= T; i++) {
        int A; //ini_pencil
        int B; //ini_sharpener
        int X; //pencil_max
        int Y; //sharpener_max
        cin >> A >> B >> X >> Y;

        int C = 0; //add_pencil
        int D = 0; //add_sharpener

        //errors
        if (A<0 || A>100) {
            cout << "Error: A out of range";
            exit(1);
        }
        if (B<0 || B>100) {
            cout << "Error: B out of range";
            exit(1);
        }
        if (X<1 || X>100) {
            cout << "Error: X out of range";
            exit(1);
        }
        if (Y<1 || Y>100) {
            cout << "Error: Y out of range";
            exit(1);
        }
        int max_ini_pencil_uses = A * X;
        int max_ini_sharp_uses = B * Y;
        int sharp_leftover_uses = max_ini_sharp_uses - max_ini_pencil_uses;
        if (X == Y) {
            cout << abs((int)sharp_leftover_uses / X) << endl;
        } else {
            while (sharp_leftover_uses != 0) {
                if (sharp_leftover_uses > 0) {
                    ++C;
                    sharp_leftover_uses = sharp_leftover_uses - X;
                } else {
                    ++D;
                    sharp_leftover_uses = sharp_leftover_uses + Y;
                }
            }
            cout << C + D << endl;
        }
    }
}