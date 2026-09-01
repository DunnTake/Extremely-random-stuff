// Beginner Free Contest 52 - TOYS
// https://oj.vnoi.info/problem/fcb052_toys

#include <bits/stdc++.h>
#define int long long
using namespace std;

signed main() {
    int N; // toys
    int M; // money
    cin >> N >> M;

    int toys[N]; // value
    for (int i = 0; i < N; i++) {
        cin >> toys[i];
    }
    sort(toys,toys + N);

    int max_amount = round(((1 - sqrt(1+2*N))/-2) + 1) * 1000; //max storage
    int buying[max_amount];

    // buying function
    int inventory_item = 0;
    int bought_items = 0;
    for (int i = 1; i <= M; i++) {
        if (toys[inventory_item] == i) {
            ++inventory_item;
        } else {
            buying[bought_items] = i;
            M -= i;
            ++bought_items;
        }
    }

    // print answer
    cout << bought_items << endl;
    for (int i = 0; i < bought_items; i++) {
        cout << buying[i] << " ";
    }
    return(0);
}