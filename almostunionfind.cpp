#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

const int MAX = 200005;
int parent[MAX], cont[MAX];
ll sum[MAX];

void make_set ( int n ) {
    for ( int i = 1, j = n + 1; i <= n; ++i, ++j ) {
        parent[i] = j;
        parent[j] = j;
        cont[j] = 1;
        sum[j] = i;
    }
}

int find ( int x ) {
    if ( parent[x] == x ) return x;
    return parent[x] = find(parent[x]);
}

void merge ( int x, int y ) {
    x = find(x);
    y = find(y);
    if ( x != y ) {
        cont[y] += cont[x];
        sum[y] += sum[x];
        parent[x] = y;
    }
}

void move ( int x, int y ) {
    int x_root = find(x);
    int y_root = find(y);
    if ( x_root != y_root ) {
        ++cont[y_root];
        --cont[x_root];
        sum[y_root] += x;
        sum[x_root] -= x;
        parent[x] = y_root;
    }
}

int main ( ) {
    int n, m, cmd, p, q;
    while ( cin >> n >> m ) {
        make_set(n);
        for ( int i = 0; i < m; ++i ) {
            cin >> cmd;
            if ( cmd == 1 ) {
                cin >> p >> q;
                merge(p, q);
            } else if ( cmd == 2 ) {
                cin >> p >> q;
                move(p, q);
            } else {
                cin >> p;
                cout << cont[find(p)] << ' ' << sum[find(p)] << '\n';
            }
        }
    }
}