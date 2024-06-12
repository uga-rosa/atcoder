#include <atcoder/all>
#include <bits/stdc++.h>
using namespace std;
using namespace atcoder;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using ll = int64_t;

int main() {
  int n, k;
  cin >> n >> k;
  vector<int> a(n);
  rep(i, n) cin >> a[i];

  int c = 0;
  // 今アトラクションに乗っている人数
  int num = 0;
  rep(i, n) {
    if (num + a[i] > k) {
      // スタート
      c++;
      num = a[i];
    } else {
      num += a[i];
    }
  }
  // 待機列空になったので最後のスタート
  c++;
  cout << c << endl;
}
