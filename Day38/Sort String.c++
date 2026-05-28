#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>
#include <algorithm>

using namespace std;

// User logic function declaration
string user_logic(const string& S);

int main() {

    string S;

    getline(cin, S);

    // Call user logic function and print the output
    string result = user_logic(S);

    cout << result << endl;

    return 0;
}

// User logic function definition
string user_logic(const string& S) {

    unordered_map<char, int> freq;

    // Count frequency
    for (char ch : S) {
        freq[ch]++;
    }

    // Store characters
    vector<pair<char, int>> arr;

    for (auto &it : freq) {
        arr.push_back({it.first, it.second});
    }

    sort(arr.begin(), arr.end(), [](pair<char, int> a, pair<char, int> b) {

        if (a.second == b.second) {
            return a.first < b.first;
        }

        return a.second > b.second;
    });

    string ans = "";

    // Build answer
    for (auto &p : arr) {

        ans += string(p.second, p.first);
    }

    return ans;
}
    