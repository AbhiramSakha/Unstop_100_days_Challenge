#include <iostream>
using namespace std;

const int MOD = 1000000007;

int numOfWays(int n) {
    long long same = 6;   // ABA pattern
    long long diff = 6;   // ABC pattern

    for (int i = 2; i <= n; i++) {
        long long newSame = (3 * same + 2 * diff) % MOD;
        long long newDiff = (2 * same + 2 * diff) % MOD;
        same = newSame;
        diff = newDiff;
    }

    return (same + diff) % MOD;
}

int main() {
    int n;
    cin >> n;

    cout << numOfWays(n) << endl;
    return 0;
}