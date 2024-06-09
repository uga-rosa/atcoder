#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
  int N, Q, t, x, y, s, tmp;
  cin >> N >> Q;
  vector<int> A(N);
  rep(i, N) cin >> A.at(i);
  s = 0;

  rep(i, Q) {
    cin >> t >> x >> y;
    x = pow_mod(x-1-s, 1, N);
    y = pow_mod(y-1-s, 1, N);
    if (t == 1) {
      swap(A[x], A[y]);
    } else if (t == 2) {
      s++;
    } else {
      cout << A.at(x) << endl;
    }
  }
}
