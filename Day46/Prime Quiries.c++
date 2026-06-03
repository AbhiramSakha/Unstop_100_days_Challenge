#include <iostream>
#include <vector>
#include <string>

std::string process_queries(int q, const std::vector<int>& queries) {
    int maxVal = 100000;

    std::vector<bool> isPrime(maxVal + 1, true);
    isPrime[0] = isPrime[1] = false;

    for (int i = 2; i * i <= maxVal; i++) {
        if (isPrime[i]) {
            for (int j = i * i; j <= maxVal; j += i) {
                isPrime[j] = false;
            }
        }
    }

    std::string ans;
    ans.reserve(q);

    for (int x : queries) {
        ans.push_back(isPrime[x] ? '1' : '0');
    }

    return ans;
}

int main() {
    int q;
    std::cin >> q;
    std::vector<int> queries(q);
    for (int i = 0; i < q; ++i) {
        std::cin >> queries[i];
    }
    std::string result = process_queries(q, queries);
    std::cout << result << std::endl;
    return 0;
}