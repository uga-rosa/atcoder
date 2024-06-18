#include <atcoder/all>
using namespace atcoder;
#include <bits/stdc++.h>
using namespace std;

#define rep(i, l, r) for (ll i = (l); i < (ll)(r); i++)
#define all(...) std::begin(__VA_ARGS__), std::end(__VA_ARGS__)
#define rall(...) std::rbegin(__VA_ARGS__), std::rend(__VA_ARGS__)
using ll = long long;
template <typename T> auto vec2(int i, int j, T init = T()) {
  return vector<vector<T>>(i, vector<T>(j));
}
ll pow(ll x, ll n) {
  ll ans = 1;
  while (n > 0) {
    if (n & 1)
      ans *= x;
    x *= x;
    n >>= 1;
  }
  return ans;
}

int main() {
  int n, x, y;
  cin >> n;
  auto c = vec2(n, 0, 0);
  rep(i, 0, n) {
    cin >> x >> y;
    c[i] = {x, y};
  }

  rep(i, 0, n) {
    int dist2, d, id;
    dist2 = 0;
    rep(j, 0, n) {
      d = pow(c[i][0] - c[j][0], 2) + pow(c[i][1] - c[j][1], 2);
      if (d > dist2) {
        dist2 = d;
        id = j + 1;
      }
    }
    cout << id << endl;
  }
}
