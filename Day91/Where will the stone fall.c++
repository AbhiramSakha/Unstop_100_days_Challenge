#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int m, n;
    cin >> m >> n;

    vector<vector<int>> grid(m, vector<int>(n));
    for (int i = 0; i < m; i++)
        for (int j = 0; j < n; j++)
            cin >> grid[i][j];

    for (int start = 0; start < n; start++) {
        int col = start;
        bool stuck = false;

        for (int row = 0; row < m; row++) {
            int nextCol = col + grid[row][col];

            if (nextCol < 0 || nextCol >= n || grid[row][nextCol] != grid[row][col]) {
                stuck = true;
                break;
            }

            col = nextCol;
        }

        if (stuck)
            cout << -1 << " ";
        else
            cout << col << " ";
    }

    return 0;
}