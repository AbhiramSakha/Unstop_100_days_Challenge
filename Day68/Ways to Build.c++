#include <iostream>
#include <vector>
using namespace std;

#define MOD 1000000007

int num_of_arrays(int n, int m, int k) {
    vector<vector<long long>> dp(k + 2, vector<long long>(m + 1, 0));

    // First element
    for (int mx = 1; mx <= m; mx++)
        dp[1][mx] = 1;

    // Remaining positions
    for (int pos = 2; pos <= n; pos++) {
        vector<vector<long long>> ndp(k + 2, vector<long long>(m + 1, 0));

        for (int cost = 1; cost <= k; cost++) {
            for (int mx = 1; mx <= m; mx++) {
                if (dp[cost][mx] == 0) continue;

                // Pick a value <= current maximum
                ndp[cost][mx] =
                    (ndp[cost][mx] + dp[cost][mx] * mx) % MOD;

                // Pick a new maximum
                if (cost < k) {
                    for (int nmx = mx + 1; nmx <= m; nmx++) {
                        ndp[cost + 1][nmx] =
                            (ndp[cost + 1][nmx] + dp[cost][mx]) % MOD;
                    }
                }
            }
        }

        dp.swap(ndp);
    }

    long long ans = 0;
    for (int mx = 1; mx <= m; mx++)
        ans = (ans + dp[k][mx]) % MOD;

    return (int)ans;
}

int main() {
    int n, m, k;
    cin >> n >> m >> k;

    cout << num_of_arrays(n, m, k) << endl;
    return 0;
}