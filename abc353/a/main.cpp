#include <atcoder/all>
#include <bits/stdc++.h>
using namespace std;
using namespace atcoder;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using ll = int64_t;

int main() {
  int n, left;
  cin >> n;
  vector<int> h(n);
  rep(i, n) cin >> h[i];

  left = h[0];
  for (int i = 1; i < n; i++) {
    if (h[i] > left) {
      cout << i + 1 << endl;
      return 0;
    }
  }
  cout << -1 << endl;
}
