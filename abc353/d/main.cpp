#include <atcoder/all>
#include <bits/stdc++.h>
using namespace std;
using namespace atcoder;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using ll = int64_t;
const int MOD = 998244353;

ll pow10_digit(int x) {
  ll ans = 1;
  while (x > 0) {
    ans *= 10;
    x /= 10;
  }
  return ans;
}

int main() {
  int n;
  cin >> n;
  vector<int> a(n);
  rep(i, n) cin >> a[i];

  vector<ll> pow10_digit_sum_r(n + 1, 0);
  for (int i = n - 1; i >= 0; i--) {
    pow10_digit_sum_r[i] = (pow10_digit_sum_r[i + 1] + pow10_digit(a[i])) % MOD;
  }

  ll ans = 0;
  rep(i, n) {
    ans += a[i] * (i + pow10_digit_sum_r[i + 1]);
    ans %= MOD;
  }
  cout << ans << endl;
}
