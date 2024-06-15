#include <atcoder/all>
#include <bits/stdc++.h>
using namespace std;
using namespace atcoder;

using ll = long long;
#define rep(i, l, r) for (ll i = (l); i < (ll)(r); i++)
#define all(...) std::begin(__VA_ARGS__), std::end(__VA_ARGS__)
#define rall(...) std::rbegin(__VA_ARGS__), std::rend(__VA_ARGS__)
#define $(idx) (std::get<(idx)>(std::forward_as_tuple(_args...)))
#define lambda(...) ([&](auto &&..._args) { return (__VA_ARGS__); })
const ll n = (ll)1 << 60;
vector<pair<ll, ll>> ans(0);

void rec(ll ql, ll qr, ll sl = 0, ll sr = n) {
  if (sr <= ql || qr <= sl) {
    return;
  } else if (ql <= sl && sr <= qr) {
    ans.push_back({sl, sr});
    return;
  }
  ll sm = (sl + sr) / 2;
  rec(ql, qr, sl, sm);
  rec(ql, qr, sm, sr);
}

int main() {
  ll l, r;
  cin >> l >> r;
  rec(l, r);
  cout << ans.size() << endl;
  for (auto [ll, rr] : ans) {
    cout << ll << " " << rr << endl;
  }
}
