#include <iostream>
#include <string>
#include <vector>

using namespace std;

int smallest_max_split(const string& s) {

    int n = s.size();

    vector<int> prefix(n, 0);
    vector<int> suffix(n, 0);

    vector<int> freq(10, 0);

    int distinct = 0;

    // Prefix distinct count
    for (int i = 0; i < n; i++) {

        int digit = s[i] - '0';

        if (freq[digit] == 0) {
            distinct++;
        }

        freq[digit]++;

        prefix[i] = distinct;
    }

    // Reset frequency
    freq.assign(10, 0);

    distinct = 0;

    // Suffix distinct count
    for (int i = n - 1; i >= 0; i--) {

        int digit = s[i] - '0';

        if (freq[digit] == 0) {
            distinct++;
        }

        freq[digit]++;

        suffix[i] = distinct;
    }

    int maxSum = -1;
    int answer = 0;

    // Try every split
    for (int i = 0; i < n - 1; i++) {

        int current = prefix[i] + suffix[i + 1];

        if (current > maxSum) {
            maxSum = current;
            answer = i;
        }
    }

    return answer;
}

int main() {

    int n;
    string s;

    cin >> n >> s;

    int result = smallest_max_split(s);

    cout << result << endl;

    return 0;
}
     