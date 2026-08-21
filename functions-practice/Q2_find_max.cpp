#include <iostream>
using namespace std;

int findMax(int a, int b) {
    if (a > b) {
        return a;
    }
    return b;
}

int main() {
    int a, b;
    cin >> a >> b;

    int result = findMax(a, b);
    cout << "Maximum = " << result << endl;

    return 0;
}
