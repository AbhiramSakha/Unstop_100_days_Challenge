#include <iostream>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    vector<long long> arr(N);

    long long answer = 0;
    for (int i = 0; i < N; i++) {
        cin >> arr[i];
        answer += arr[i]; // book retrieval time
    }

    long long prefMax = 0;

    for (int i = 0; i < N; i++) {
        if (arr[i] > prefMax) {
            answer += (long long)(N - i) * (arr[i] - prefMax);
            prefMax = arr[i];
        }
    }

    cout << answer << '\n';
    return 0;
}