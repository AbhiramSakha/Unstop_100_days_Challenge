#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int main() {
    int N;
    cin >> N;  // Read the size of the array

    vector<int> arr(N);
    for (int i = 0; i < N; ++i) {
        cin >> arr[i];  // Read the array elements
    }

    // Initialize prefix XOR array
    vector<int> prefix(N + 1, 0);  // prefix[i] holds XOR of elements from 0 to i-1
    for (int i = 0; i < N; ++i) {
        prefix[i + 1] = prefix[i] ^ arr[i];  // prefix XOR up to index i
    }

    long long SE = 0;  // Sum of XORs for even-length subarrays
    long long SO = 0;  // Sum of XORs for odd-length subarrays

    // Calculate XOR for all subarrays
    for (int i = 0; i < N; ++i) {
        for (int j = i + 1; j <= N; ++j) {
            int subarrayXOR = prefix[j] ^ prefix[i];  // XOR of subarray arr[i...j-1]
            if ((j - i) % 2 == 0) {  // Even-length subarray
                SE += subarrayXOR;
            } else {  // Odd-length subarray
                SO += subarrayXOR;
            }
        }
    }

    // Calculate the golden value G
    long long G = abs(SE - SO);
    cout << G << endl;  // Output the golden value G

    return 0;
}