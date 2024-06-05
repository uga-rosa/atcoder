#include <bits/stdc++.h>
using namespace std;

int main() {
  vector<int> A(5);
  for (int i = 0; i < 5; i++) {
    cin >> A.at(i);
  }

  for (int i = 0; i < A.size()-1; i++) {
    if (A[i] == A[i+1]) {
      cout << "YES" << endl;
      return 0;
    }
  }
  cout << "NO" << endl;
}
