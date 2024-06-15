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
  int n, a, b;
  cin >> n;
  vector<pair<int, int>> giants(n);
  rep(i, n) {
    cin >> a >> b;
    giants[i] = {b - a, a};
  }
  sort(all(giants));
  ll ans = 0;
  rep(i, n) ans += giants[i].second;
  ans += giants[n - 1].first;
  cout << ans << endl;
}
