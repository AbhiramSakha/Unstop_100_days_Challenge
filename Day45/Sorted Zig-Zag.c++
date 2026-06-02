#include <iostream>
#include <vector>
#include <algorithm>

void user_logic(int n, std::vector<int> &arr, std::vector<std::vector<int>> &result) {
    std::sort(arr.begin(), arr.end());

    int idx = 0;
    int level = 0;
    int nodesInLevel = 1;

    while (idx < n) {
        std::vector<int> curr;

        for (int i = 0; i < nodesInLevel && idx < n; i++) {
            curr.push_back(arr[idx++]);
        }

        if (level % 2 == 1) {
            std::reverse(curr.begin(), curr.end());
        }

        result.push_back(curr);

        nodesInLevel *= 2;
        level++;
    }
}

int main() {
    int n;
    std::cin >> n;

    std::vector<int> arr(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> arr[i];
    }

    std::vector<std::vector<int>> result;
    user_logic(n, arr, result);

    for (const auto &row : result) {
        for (size_t i = 0; i < row.size(); ++i) {
            if (i > 0) std::cout << " ";
            std::cout << row[i];
        }
        std::cout << std::endl;
    }

    return 0;
}