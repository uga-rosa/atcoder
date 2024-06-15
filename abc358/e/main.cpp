#include <atcoder/all>
using namespace atcoder;
#include <bits/stdc++.h>
using namespace std;

#define rep(i, l, r) for (int i = (l); i < (int)(r); i++)
using ll = long long;
using mint = modint998244353;
unordered_map<int, mint> memo;

mint comb(int n, int r) {
  if (n == r || r == 0) {
    return 1;
  }
  auto key = 1000 * n + r;
  if (memo[key] != 0) {
    return memo[key];
  }
  memo[key] = comb(n - 1, r) + comb(n - 1, r - 1);
  return memo[key];
}

int main() {
  int K;
  cin >> K;
  vector<int> C(26);
  rep(i, 0, 26) cin >> C[i];

  // dp[i][j] := c[i]まで使ってj文字の文字列は何通り作れるか
  vector<vector<mint>> dp(27, vector(K + 1, mint(0)));
  dp[0][0] = 1;
  rep(i, 0, 26) rep(j, 0, K + 1) rep(k, 0, min(j, C[i]) + 1) {
    dp[i + 1][j] += comb(j, k) * dp[i][j - k];
  }

  mint ans = 0;
  rep(i, 1, K + 1) { ans += dp[26][i]; }
  cout << ans.val() << endl;
}
