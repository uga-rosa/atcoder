#include <atcoder/all>
#include <bits/stdc++.h>
using namespace std;
using namespace atcoder;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
const int MOD = 1000000007;

int main() {
  int N, L;
  cin >> N >> L;

  // dp[i] := i段目にたどり着ける移動方法の総数
  vector<int> dp(N + 1);
  dp[0] = 1;
  rep(i, N) {
    dp[i + 1] += dp[i];
    dp[i + 1] %= MOD;
    if (i + L <= N) {
      dp[i + L] += dp[i];
      dp[i + L] %= MOD;
    }
  }

  cout << dp[N] << endl;
}
