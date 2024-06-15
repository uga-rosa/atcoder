#include <atcoder/all>
#include <bits/stdc++.h>
using namespace std;
using namespace atcoder;

using ll = int64_t;
#define WRAP_REP(_1, _2, _3, NAME, ...) NAME
#define REP2(i, n) for (ll i = 0; i < (ll)(n); i++)
#define REP3(i, l, r) for (ll i = (l); i < (ll)(r); i++)
#define rep(...) WRAP_REP(__VA_ARGS__, REP3, REP2)(__VA_ARGS__)
#define all(...) std::begin(__VA_ARGS__), std::end(__VA_ARGS__)
#define rall(...) std::rbegin(__VA_ARGS__), std::rend(__VA_ARGS__)
#define $(idx) (std::get<(idx)>(std::forward_as_tuple(_args...)))
#define lambda(...) ([&](auto &&..._args) { return (__VA_ARGS__); })

int main() {
  int n, m, k, c, a0, a;
  cin >> n >> m;
  map<int, vector<pair<int, int>>> cost_to_pairs;
  rep(_, m) {
    cin >> k >> c >> a0;
    a0--;
    rep(_, 1, k) {
      cin >> a;
      cost_to_pairs[c].push_back({a0, a - 1});
    }
  }

  ll ans = 0;
  dsu uf(n);
  for (auto cp : cost_to_pairs) {
    for (auto &p : cp.second) {
      if (!uf.same(p.first, p.second)) {
        ans += cp.first;
        uf.merge(p.first, p.second);
      }
    }
  }
  if (uf.size(0) == n) {
    cout << ans << endl;
  } else {
    cout << -1 << endl;
  }
}
