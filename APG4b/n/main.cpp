#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
  int N;
  cin >> N;
  vector<int> A(N);
  rep(i, N) {
    cin >> A[i];
  }

  int ave = reduce(A.begin(), A.end()) / N;
  rep(i, N) {
    cout << abs(A[i] - ave) << endl;
  }
}
