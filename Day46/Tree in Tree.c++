#include <iostream>
#include <vector>
#include <functional>
using namespace std;

static const int MOD = 998244353;

vector<int> user_logic(int n, vector<pair<int, int>>& edges) {
    vector<vector<int>> adj(n + 1);
    for (auto &e : edges) {
        int u = e.first, v = e.second;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    vector<int> sz(n + 1, 0);

    function<pair<vector<int>, vector<int>>(int, int)> dfs =
        [&](int u, int p) -> pair<vector<int>, vector<int>> {

        vector<int> dp0(1, 1); // u not selected, 0 components
        vector<int> dp1(2, 0); // u selected, 1 component
        dp1[1] = 1;

        sz[u] = 1;

        for (int v : adj[u]) {
            if (v == p) continue;

            auto child = dfs(v, u);
            vector<int> &g0 = child.first;
            vector<int> &g1 = child.second;

            int curSize = sz[u];
            int childSize = sz[v];

            vector<int> ndp0(curSize + childSize + 1, 0);
            vector<int> ndp1(curSize + childSize + 1, 0);

            // Merge into dp0 (u not selected)
            for (int i = 0; i < (int)dp0.size(); i++) {
                if (!dp0[i]) continue;

                for (int j = 0; j < (int)g0.size(); j++) {
                    if (!g0[j]) continue;
                    ndp0[i + j] = (ndp0[i + j] + (long long)dp0[i] * g0[j]) % MOD;
                }

                for (int j = 0; j < (int)g1.size(); j++) {
                    if (!g1[j]) continue;
                    ndp0[i + j] = (ndp0[i + j] + (long long)dp0[i] * g1[j]) % MOD;
                }
            }

            // Merge into dp1 (u selected)
            for (int i = 0; i < (int)dp1.size(); i++) {
                if (!dp1[i]) continue;

                // child root not selected
                for (int j = 0; j < (int)g0.size(); j++) {
                    if (!g0[j]) continue;
                    ndp1[i + j] = (ndp1[i + j] + (long long)dp1[i] * g0[j]) % MOD;
                }

                // child root selected -> merge one component through edge (u,v)
                for (int j = 0; j < (int)g1.size(); j++) {
                    if (!g1[j]) continue;
                    ndp1[i + j - 1] =
                        (ndp1[i + j - 1] + (long long)dp1[i] * g1[j]) % MOD;
                }
            }

            dp0.swap(ndp0);
            dp1.swap(ndp1);
            sz[u] += childSize;
        }

        return {dp0, dp1};
    };

    auto rootDP = dfs(1, 0);
    vector<int> ans(n, 0);

    for (int k = 1; k <= n; k++) {
        long long res = 0;

        if (k < (int)rootDP.first.size()) res += rootDP.first[k];
        if (k < (int)rootDP.second.size()) res += rootDP.second[k];

        ans[k - 1] = (int)(res % MOD);
    }

    return ans;
}

int main() {
    int n;
    cin >> n;

    vector<pair<int, int>> edges(n - 1);
    for (int i = 0; i < n - 1; ++i) {
        cin >> edges[i].first >> edges[i].second;
    }

    vector<int> results = user_logic(n, edges);

    for (int x : results) {
        cout << x << '\n';
    }

    return 0;
}