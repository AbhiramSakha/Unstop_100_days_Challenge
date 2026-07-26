#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void solve(vector<int>& arr, int d) {
    int n = arr.size();
    vector<int> dp(n, 1);

    vector<int> idx(n);
    for (int i = 0; i < n; i++) idx[i] = i;

    sort(idx.begin(), idx.end(), [&](int a, int b) {
        return arr[a] < arr[b];
    });

    int ans = 1;

    for (int id : idx) {
        // Left
        for (int j = id - 1; j >= max(0, id - d); j--) {
            if (arr[j] >= arr[id]) break;
            dp[id] = max(dp[id], dp[j] + 1);
        }

        // Right
        for (int j = id + 1; j <= min(n - 1, id + d); j++) {
            if (arr[j] >= arr[id]) break;
            dp[id] = max(dp[id], dp[j] + 1);
        }

        ans = max(ans, dp[id]);
    }

    cout << ans;
}

int main() {
    int n, d;
    cin >> n >> d;
    vector<int> arr(n);
    for (int i = 0; i < n; ++i) {
        cin >> arr[i];
    }
    solve(arr, d);
    return 0;
}