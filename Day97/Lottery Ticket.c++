#include <iostream>
#include <vector>
#include <deque>
using namespace std;

vector<int> LuckyArray(vector<int>& arr, int n) {
    vector<int> a;
    for (int x : arr) {
        if (x >= 0)
            a.push_back(x);
    }

    int m = a.size();
    vector<int> ans;

    for (int k = 1; k <= m; k++) {
        deque<int> dq;
        int best = -1000000000;

        for (int i = 0; i < m; i++) {
            while (!dq.empty() && a[dq.back()] >= a[i])
                dq.pop_back();

            dq.push_back(i);

            while (!dq.empty() && dq.front() <= i - k)
                dq.pop_front();

            if (i >= k - 1)
                best = max(best, a[dq.front()]);
        }

        ans.push_back(best);
    }

    return ans;
}

int main() {
    int n;
    cin >> n;

    vector<int> arr(n);
    for (int i = 0; i < n; ++i)
        cin >> arr[i];

    vector<int> result = LuckyArray(arr, n);

    for (int num : result)
        cout << num << " ";

    cout << endl;
    return 0;
}