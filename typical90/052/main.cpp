#include <atcoder/all>
#include <bits/stdc++.h>
using namespace std;
using namespace atcoder;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
const int MOD = 1000000007;

int main() {
  int N, a1, a2, a3, a4, a5, a6;
  cin >> N;
  int64_t ans = 1;
  rep(i, N) {
    cin >> a1 >> a2 >> a3 >> a4 >> a5 >> a6;
    ans *= a1 + a2 + a3 + a4 + a5 + a6;
    ans %= MOD;
  }
  cout << ans << endl;
}
