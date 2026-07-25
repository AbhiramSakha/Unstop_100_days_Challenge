#include <iostream>
#include <vector>
using namespace std;

int user_logic(int n, int m, vector<vector<int>>& grid) {
    // Flip rows so that first column is all 1s
    for (int i = 0; i < n; i++) {
        if (grid[i][0] == 0) {
            for (int j = 0; j < m; j++)
                grid[i][j] ^= 1;
        }
    }

    // Compute maximum possible score
    long long score = 0;
    for (int j = 0; j < m; j++) {
        int ones = 0;
        for (int i = 0; i < n; i++)
            ones += grid[i][j];

        ones = max(ones, n - ones);
        score += 1LL * ones * (1LL << (m - j - 1));
    }

    if (score < 2) return 0;

    // Count primes <= score using linear sieve
    int limit = (int)score;
    vector<bool> isPrime(limit + 1, true);
    isPrime[0] = isPrime[1] = false;

    for (long long i = 2; i * i <= limit; i++) {
        if (isPrime[i]) {
            for (long long j = i * i; j <= limit; j += i)
                isPrime[j] = false;
        }
    }

    int cnt = 0;
    for (int i = 2; i <= limit; i++)
        if (isPrime[i]) cnt++;

    return cnt;
}

int main() {
    int n, m;
    cin >> n >> m;

    vector<int> elements(n * m);
    for (int i = 0; i < n * m; i++)
        cin >> elements[i];

    vector<vector<int>> grid(n, vector<int>(m));
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            grid[i][j] = elements[i * m + j];

    cout << user_logic(n, m, grid) << endl;
    return 0;
}