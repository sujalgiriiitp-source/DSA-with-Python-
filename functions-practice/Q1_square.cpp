#include <iostream>
using namespace std;

int square(int n) {
    return n * n;
}

int main() {
    int n;
    cin >> n;

    int result = square(n);
    cout << "Square = " << result << endl;

    return 0;
}
