#include <iostream>
#include <vector>
#include <string>
#include <unordered_set>

int user_logic(const std::string& s) {
    std::unordered_set<std::string> st;

    for (int i = 0; i < (int)s.size() - 1; ++i) {
        st.insert(s.substr(i, 2));
    }

    return st.size();
}

int main() {
    int T;
    std::cin >> T;
    std::vector<int> results(T);
    
    for (int i = 0; i < T; ++i) {
        std::string S;
        std::cin >> S;
        results[i] = user_logic(S);
    }
    
    for (const auto& res : results) {
        std::cout << res << std::endl;
    }
    
    return 0;
}
           