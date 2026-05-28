#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int longest_common_string_length(const vector<string>& strings) {

    vector<int> common(26, 1000000);

    for (const string& s : strings) {

        vector<int> freq(26, 0);

        for (char ch : s) {
            freq[ch - 'a']++;
        }

        for (int i = 0; i < 26; i++) {
            common[i] = min(common[i], freq[i]);
        }
    }

    int ans = 0;

    for (int i = 0; i < 26; i++) {
        ans += common[i];
    }

    return ans;
}

int main() {

    int n;
    cin >> n;

    vector<string> strings(n);

    for (int i = 0; i < n; ++i) {
        cin >> strings[i];
    }

    int result = longest_common_string_length(strings);

    cout << result << endl;

    return 0;
}
  