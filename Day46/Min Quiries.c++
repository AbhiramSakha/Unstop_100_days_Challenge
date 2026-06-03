#include <iostream>
#include <vector>

std::vector<int> user_logic(int n, int m, std::vector<int>& arr, std::vector<int>& queries) {
    std::vector<int> prefixMin(n);
    prefixMin[0] = arr[0];

    for (int i = 1; i < n; i++) {
        prefixMin[i] = std::min(prefixMin[i - 1], arr[i]);
    }

    std::vector<int> ans;
    ans.reserve(m);

    for (int i = 0; i < m; i++) {
        ans.push_back(prefixMin[queries[i]]);
    }

    return ans;
}

int main() {
    int n, m;
    std::cin >> n >> m;
    
    std::vector<int> arr(n);
    std::vector<int> queries(m);
    
    for (int i = 0; i < n; ++i) {
        std::cin >> arr[i];
    }
    for (int i = 0; i < m; ++i) {
        std::cin >> queries[i];
    }
    
    std::vector<int> result = user_logic(n, m, arr, queries);
    
    for (int i = 0; i < result.size(); ++i) {
        std::cout << result[i] << " ";
    }
    std::cout << std::endl;
    
    return 0;
}