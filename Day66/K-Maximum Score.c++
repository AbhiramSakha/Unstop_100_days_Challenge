#include <iostream>
#include <vector>
using namespace std;

long long solve(vector<int>& nums) {
    int n = nums.size();
    long long ans = 0;
    int left = 0;
    int mask = 0;

    for (int right = 0; right < n; right++) {
        while ((mask & nums[right]) != 0) {
            mask ^= nums[left];
            left++;
        }
        mask |= nums[right];

        int len = right - left + 1;
        if (len >= 2) ans += (len - 1);
    }

    return ans;
}

int main() {
    int n;
    cin >> n;

    vector<int> v(n);
    for (int &x : v) cin >> x;

    cout << solve(v) << endl;
    return 0;
}