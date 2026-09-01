// Bedao Mini Contest 06 - GIRLS
// https://oj.vnoi.info/problem/bedao_m06_girls

#include <bits/stdc++.h>
#define int long long
using namespace std;

signed main() {
    int M; // girls
    int N; // number of chosen girls
    int K; // scoring difference limit

    cin >> M >> N >> K;

    int girls[M];
    for (int i = 0; i < M; i++) {
        cin >> girls[i];
    }
    sort(girls, girls + M, greater<>()); 

    int pick[N];
    for (int i = 0; i <= M - N; i++) {
        if ((girls[i] - girls[i+N-1]) <= K) {
            int total = 0;
            for (int k = 0; k < N; k++){
                total += girls[i+k];
            }
            cout << total;
            return 0;
        } 
    }
    cout << -2;
    return 0;
}