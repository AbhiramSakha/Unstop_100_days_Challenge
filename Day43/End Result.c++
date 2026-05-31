#include <iostream>
#include <vector>
using namespace std;

int user_logic(int a, int b) {
    int matches[] = {6, 2, 5, 5, 4, 5, 6, 3, 7, 6};

    int sum = a + b;
    int total = 0;

    while (sum > 0) {
        total += matches[sum % 10];
        sum /= 10;
    }

    return total;
}

int main() {
    int T;
    cin >> T;

    vector<int> results(T);

    for (int i = 0; i < T; i++) {
        int A, B;
        cin >> A >> B;
        results[i] = user_logic(A, B);
    }

    for (int res : results) {
        cout << res << endl;
    }

    return 0;
}
