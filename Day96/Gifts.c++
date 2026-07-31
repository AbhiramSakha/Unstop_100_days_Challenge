#include <bits/stdc++.h>
using namespace std;

const int MOD = 1000000007;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    vector<vector<int>> owners(201);

    for (int i = 0; i < N; i++) {
        int k;
        cin >> k;
        while (k--) {
            int x;
            cin >> x;
            owners[x].push_back(i);
        }
    }

    int M = 1 << N;
    vector<long long> dp(M, 0), ndp(M, 0);
    dp[0] = 1;

    for (int gift = 1; gift <= 200; gift++) {
        ndp = dp;  // skip this gift

        for (int mask = 0; mask < M; mask++) {
            if (dp[mask] == 0) continue;

            for (int f : owners[gift]) {
                if ((mask & (1 << f)) == 0) {
                    int nmask = mask | (1 << f);
                    ndp[nmask] = (ndp[nmask] + dp[mask]) % MOD;
                }
            }
        }

        dp.swap(ndp);
    }

    cout << dp[M - 1] % MOD << '\n';
    return 0;
}