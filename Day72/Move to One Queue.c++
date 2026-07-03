#include <iostream>
#include <vector>
using namespace std;

int min_cost_to_move_to_queue(vector<int>& pos) {
    int even = 0, odd = 0;

    for (int x : pos) {
        if (x % 2 == 0)
            even++;
        else
            odd++;
    }

    return min(even, odd);
}

int main() {
    int n;
    cin >> n;

    vector<int> pos(n);
    for (int i = 0; i < n; ++i) {
        cin >> pos[i];
    }

    cout << min_cost_to_move_to_queue(pos) << endl;

    return 0;
}