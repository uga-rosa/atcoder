#include <atcoder/all>
#include <bits/stdc++.h>
using namespace std;
using namespace atcoder;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using ll = uint64_t;
const int MOD = 100000;

int dig_sum(int x) {
  int ans = 0;
  while (x > 0) {
    ans += x % 10;
    x /= 10;
  }
  return ans;
}

int main() {
  int n;
  ll k;
  cin >> n >> k;
  // 状態Nが10**5しかないのですぐループするはず
  int loop_start = 0;
  ll loop_size = MOD;
  vector<int> n_to_i(MOD, -1);
  vector<int> i_to_n(MOD, -1);
  for (int i = 1; i <= k; i++) {
    n = (n + dig_sum(n)) % MOD;
    if (n_to_i[n] != -1) {
      // ループ発見
      loop_start = n_to_i[n];
      loop_size = i - n_to_i[n];
      break;
    }
    n_to_i[n] = i;
    i_to_n[i] = n;
  }
  k -= loop_start;
  k %= loop_size;
  cout << i_to_n[k + loop_start] << endl;
}
