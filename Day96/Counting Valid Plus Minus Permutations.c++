#include <iostream>
#include <vector>
#include <string>
using namespace std;

const int MOD = 1000000007;

int numPlusMinusSequence(const string &S) {
    int n = S.size();
    vector<long long> dp(n + 1, 1);

    for (int i = 0; i < n; i++) {
        vector<long long> ndp(n + 1, 0);

        if (S[i] == '+') {
            long long cur = 0;
            for (int j = 0; j < n - i; j++) {
                cur = (cur + dp[j]) % MOD;
                ndp[j] = cur;
            }
        } else { // '-'
            long long cur = 0;
            for (int j = n - i - 1; j >= 0; j--) {
                cur = (cur + dp[j + 1]) % MOD;
                ndp[j] = cur;
            }
        }

        dp = ndp;
    }

    return dp[0];
}

int main() {
    string S;
    cin >> S;

    cout << numPlusMinusSequence(S) << endl;
    return 0;
}