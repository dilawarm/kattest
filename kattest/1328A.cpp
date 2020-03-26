#include <bits/stdc++.h>
using namespace std;
 
int main() {
    int t; cin >> t;
    for (int i = 0; i < t; ++i) {
        int a, b; cin >> a >> b;
        int k = -a % b;
        while (k < 0) k += b;
        cout << k << endl;
    }
    return 0;
}