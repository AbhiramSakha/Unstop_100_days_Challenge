#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

void kth_next_permutation(int n, vector<string>& arr, int k) {
    long long fact = 1;

    for (int i = 2; i <= n; i++) {
        if (fact > k / i) {
            fact = (long long)k + 1;
            break;
        }
        fact *= i;
    }

    if (fact <= k)
        k %= fact;

    while (k--) {
        next_permutation(arr.begin(), arr.end());
    }
}

int main() {
    int n, k;
    cin >> n;

    vector<string> arr(n);
    for (int i = 0; i < n; i++)
        cin >> arr[i];

    cin >> k;

    kth_next_permutation(n, arr, k);

    for (int i = 0; i < n; i++) {
        if (i) cout << " ";
        cout << arr[i];
    }

    return 0;
}