#include <bits/stdc++.h>
using namespace std;

int main() {
  int N, A;
  cin >> N >> A;

  for (int i = 1; i < N+1; i++) {
    int B;
    string op;
    cin >> op >> B;

    if (op == "+") {
      A += B;
    } else if (op == "-") {
      A -= B;
    } else if (op == "*") {
      A *= B;
    } else if (B != 0) {
      A /= B;
    } else {
      cout << "error" << endl;
      break;
    }
    cout << i << ":" << A << endl;
  }
}
